from neuralintents import GenericAssistant




flag = 20
flag2 = 40
# temp = False
# AI Helper Functions
def extractImageText():
    # global temp
    global flag
    flag = flag/2


    # def signalResponse(temp):
    #     print("You did it man!")
    # return signalResponse()
def convertImage():
    global flag2
    flag2 = flag2/2

# AI functionality

mappings = {
    'extract_image_text': extractImageText,
    'convert_image_to_grayscale': convertImage
}

aibot = GenericAssistant('C:\\Users\\Sushant\\Downloads\\Python_8\\Project\AIBot\\AI_Model\\intents.json', intent_methods=mappings, model_name="aibot_model")
# aibot.train_model()
# aibot.save_model()
aibot.load_model("C:\\Users\\Sushant\\Downloads\\Python_8\\Project\AIBot\\AI_Model\\aibot_model")

def ai_response(msg_response):
    return aibot.request(msg_response)



print("AiBot Started!")


if __name__ == "__main__":
    for i in range(5):
        msg = input("Enter your message: ")
        res = ai_response(msg)
        # print(res)
        # print(flag)
        if(flag==10):
            print("You are good to go!")
            print(flag)
            flag = flag*2
        elif(flag2==20):
            print("You are in flag2!")
            print(flag2)
            flag2 = flag2*2
        else: 
            print("Something went wrong!")
            print(flag)
        print(f"flag one value: {flag}")
        print("flag two value: {}".format(flag2))



