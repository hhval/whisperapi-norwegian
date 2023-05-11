import os
import sys
import openai
import transcribe_utils
import summarize_utils

openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    file_name = sys.argv[1]
    name, extension = os.path.splitext(file_name)
    
    # Transcribe the audio file using Whisper
    no_transcription = transcribe_utils.transcribe_file(file_name)
    transcribe_utils.print_file(no_transcription, name + "_transcription.txt")
    print('File transcribed')
    
    # Proofread full transcription with GPT-4
    proofed = transcribe_utils.proof_transcription(no_transcription)
    transcribe_utils.print_file(proofed, name + "_proofed.txt")
    print('Transcription proofed')

    # Create bullet point summary with GPT-4
    summary = summarize_utils.summarize(proofed)
    transcribe_utils.print_file(summary, name + "_summary.txt")
    print('Summary created')