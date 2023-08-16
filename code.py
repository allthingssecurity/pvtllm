from flask import Flask, request, jsonify
from mlc_chat import ChatModule
from mlc_chat.callback import StreamToStdout
from flask_cors import CORS
from mlc_chat import  ChatConfig, ConvConfig
# Initialize the ChatModule
conv_config = ConvConfig(system='Always return code and not just steps')
chat_config = ChatConfig(max_gen_len=1024,conv_config=conv_config)

cm = ChatModule(model="/workspace/pvtllm/dist/prebuilt/mlc-chat-WizardCoder-15B-V1.0-q4f16_1", lib_path="/workspace/pvtllm/dist/prebuilt/lib/WizardCoder-15B-V1.0-q4f16_1-cuda.so", chat_config=chat_config)

app = Flask(__name__)
# Enable CORS for all domains on all routes
CORS(app)
@app.route('/generate', methods=['POST'])
def generate():
    # Extract the input text from the POST request
    input_text = request.json.get('text')

    # Call the cm.generate method with the given input
    output = cm.generate(
        prompt=f"{input_text}",
        progress_callback=StreamToStdout(callback_interval=2),
    )

    # Return the output as JSON
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
	
	

