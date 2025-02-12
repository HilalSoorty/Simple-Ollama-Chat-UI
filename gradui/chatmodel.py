import gradio as gr
import ollama

# Set the base URL for Ollama (update this if your server is running elsewhere)
ollama.api_url = "http://localhost:11434"

def chat_with_model(history, user_input):
    """
    Update conversation history by sending a message to the Ollama model.
    The history is a list of (user, bot) message tuples.
    """
    # Append the new user message (with an empty bot reply initially)
    history.append((user_input, ""))
    
    # Prepare messages for Ollama API (you may need to format this per your model's requirements)
    messages = []
    for user_msg, bot_msg in history:
        messages.append({"role": "user", "content": user_msg})
        if bot_msg:
            messages.append({"role": "assistant", "content": bot_msg})
    
    # Send messages to the Ollama model and get a response
    response = ollama.chat(model='qwen2.5-coder:0.5b', messages=messages)
    bot_reply = response['message']['content']
    
    # Update the last entry in history with the bot's response
    history[-1] = (user_input, bot_reply)
    return history, ""

def clear_chat():
    return [], ""

# Create Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## Ollama Chatbot")
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(placeholder="Type a message...", label="Your Message")
    send_btn = gr.Button("Send")
    clear_btn = gr.Button("Clear Chat")
    state = gr.State([])  # Stores conversation history
    
    # When the button is clicked or user presses Enter, send the message.
    send_btn.click(chat_with_model, inputs=[state, user_input], outputs=[chatbot, user_input])
    user_input.submit(chat_with_model, inputs=[state, user_input], outputs=[chatbot, user_input])
    
    # Clear the chat
    clear_btn.click(clear_chat, outputs=[chatbot, user_input])
    
# Launch the interface
demo.launch()
