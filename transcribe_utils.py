import time
import openai

def transcribe_file(file_name):
    """This function transcribes a Norwegian audio file using Whisper.

    Args:
        file_name (string): Name of the file to transcribe
        Returns: string containing the Whisper transcription
    """
    tic = time.perf_counter()
    with open(file_name, "rb") as audio_file:
        no_transcript = openai.Audio.transcribe(
            model="whisper-1", 
            file=audio_file,
            language="no",
            prompt="File is mainly in Norwegian, but may contain sections in other languages. Transcribe using the Bokmål convention."
        )        
    toc = time.perf_counter()
    print(f"Transcription took {toc-tic:0.4f} seconds.")
    return no_transcript['text']

def proof_transcription(transcription):
    """This function proofreads the transcription done by Whisper using GPT-4.

    Args:
        transcription (string): Variable that contains the transcription
        Returns: string containing the fixed transcription
    """
    proofed_transcript = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[  
            {'role':'system', 'content':'You are good at proofreading text in Norwegian, and have knowledge of Norway and Norwegian. Other than fixing errors you stay as close to the original as possible.'},
            {'role':'user', 'content':f"Proofread the following Norwegian text by fixing spelling errors and changing Nynorsk words into Bokmål:\n{transcription}"}
        ]
    )
    return proofed_transcript['choices'][0]['message']['content']

def print_file(content, output_filename):
    """This function prints the transcription to a text file.

    Args:
        content (string): Name of the string to be printed to a file
        output_filename (string): Name of output file with .txt extension
        Returns: None
    """
    with open(output_filename, 'w', encoding='UTF8') as f:
        f.write(content)