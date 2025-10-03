"""
Single Interaction LLM Stream Function
This function streams responses from a Large Language Model (LLM) in real-time
with built-in streaming capability for interactive experiences.
"""

def single_interaction_llm_stream(
    prompt,
    model="tu-modelo-local",
    #temperature=0.7,
    #max_tokens=2048,
    #top_p=1.0,
):
    """
    Parameters:
    -----------
    prompt : str (required)
        The input text/question/instruction to send to the LLM.
        This is what you want the model to respond to.
        
    model : str (optional, default="tu-modelo-local")
        The name of the LLM model to use for generation.
        Examples: "gpt-4", "claude-3", "llama-2", or your local model name.
        
    #temperature : float (optional, default=0.7)
    #    Controls randomness in output (0.0 to 1.0):
    #    - Lower values (0.1-0.3): More deterministic, focused responses
    #    - Higher values (0.7-1.0): More creative, diverse responses
        
    #max_tokens : int (optional, default=2048)
    #    Maximum number of tokens (words/characters) in the response.
    #    Limits response length to prevent overly long outputs.
        
    #top_p : float (optional, default=1.0)
    #    Nucleus sampling parameter (0.0 to 1.0):
    #    - Lower values: More focused vocabulary selection
    #    - Value 1.0: Uses all possible vocabulary
        
    Returns:
    --------
    str: The complete accumulated response from the LLM
    """
    
    # Create the message structure expected by the LLM API
    # Most LLM APIs expect messages in a list of dictionaries format
    messages = [{"role": "user", "content": prompt}]
    
    # Make API call to the LLM with streaming enabled
    # The stream=True parameter makes the response come in chunks
    response = client.chat.completions.create(
        model=model,          # Which model to use
        messages=messages,    # The conversation history/messages
        #temperature=temperature,  # Controls response randomness
        #max_tokens=max_tokens,    # Limits response length
        #top_p=top_p,              # Controls vocabulary diversity
        stream=True          # ENABLES STREAMING - responses come in real-time chunks
    )
    
    # Print header for the LLM response
    # Using end="" and flush=True to ensure immediate display without newline
    print("Respuesta del LLM:\n", end="", flush=True)
    
    # Initialize empty string to accumulate the complete response
    respuesta_total = ""
    
    # Iterate through each chunk of the streaming response
    # The API sends small pieces of the response as they're generated
    for chunk in response:
        # Extract the delta (change) part from the chunk
        # Delta contains the new content being added in this chunk
        delta = getattr(chunk.choices[0], "delta", None)
        
        # Safely extract content from delta using getattr to avoid AttributeError
        # If delta exists, get its content; otherwise use empty string
        content = getattr(delta, "content", "") if delta else ""
        
        # If this chunk contains actual text content
        if content:
            # Print the content immediately without newline
            # This creates the real-time streaming effect
            print(content, end="", flush=True)
            
            # Accumulate the content to build the complete response
            respuesta_total += content
    
    # Print a final newline after streaming completes
    print()
    
    # Return the complete accumulated response
    return respuesta_total

"""
Example Usage:
---------------
# Basic usage with default model
response = single_interaction_llm_stream("Explain quantum computing")

# With custom model
response = single_interaction_llm_stream(
    prompt="Write a poem about AI",
    model="gpt-4"
)

# With all parameters (uncomment the parameters in function definition first)
# response = single_interaction_llm_stream(
#     prompt="Creative story about robots",
#     model="claude-3",
#     temperature=0.9,    # More creative
#     max_tokens=500,     # Shorter response
#     top_p=0.8          # More focused vocabulary
# )

Note: The client object must be properly initialized before using this function
Example client initialization (commented out as it depends on the specific LLM provider):
# from openai import OpenAI
# client = OpenAI(api_key="your-api-key")
"""