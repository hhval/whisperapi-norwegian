import openai

def summarize(no_transcript):
    """This function summarizes the transcription of a Norwegian newscast using bullet points.

    Args:
        no_transcript (string): Variable that contains the transcription to summarize
        Returns: string containing the summary
    """
    no_summary = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[  
            {'role':'system', 'content':'You are good at creating bullet point summaries, and have knowledge of Norway and Norwegian.'},
            {'role':'user', 'content':f"Summarize the following Norwegian text using bullet points:\n{no_transcript}"}
        ]
    )

    return no_summary['choices'][0]['message']['content']