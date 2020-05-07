# diary-generator

An excerpt from a "page" of my generated diary:

"I am able to listen to my parents talk about things and my own needs. 
Honestly, I really want to be able to listen to them, but I don't listen very much.
I think I really need to learn how to speak to my own needs. 
I think I know what I really want to know, but I haven't really communicated it to my parents very well. 
My dad doesn't like to talk to me so much, but he does talk to me occasionally. 
I think I am getting better at communicating with dad because I am reflecting back what I say to him. 
Honestly, I think I need to do more of the following: 
1. Be more present. 
Be passionate about something. 
Be passionate about math. 
Talk to more people. 
Try to keep up with habits. 
2. Respect my parents. 
Be authentic to people. 
3. Give accurate and detailed descriptions of what you are doing. 
4. Be up to speed with what you are doing. 
Learning is not just about finding what you are doing. 
It is also about being noticed."

# The Model
The heart of the diary generator is Max Woolf's gpt-2-simple model fine-tuned on 393 personal diary entries of mine.
Check out Max's blog on the model here - https://minimaxir.com/2019/09/howto-gpt2/ 
and also his documentation on gpt-2-simple here - https://github.com/minimaxir/gpt-2-simple

# How to Use
Ideally, you would have a corpus you can fine tune your gpt-2-simple model on. 
You can fine tune your gpt-2-simple model using this Google Colab notebook - https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce
Then, save the fine tuned model on your computer.

Then, download this repository and put the index.html file in a folder named 'templates'.
Add your fine-tuned model, ideally in a folder named 'checkpoint' into the repository file on your computer.

Run the 'python app.py' command on your command line to check if the flask app is working.

To deploy the model, you would need to have installed Docker and Gcloud.
You would need to create an image with Docker and then follow the steps to deploy it on Gcloud.
Here is the Medium article I used to help me: https://medium.com/datadriveninvestor/deploy-machine-learning-model-in-google-cloud-using-cloud-run-6ced8ba52aac

# The App

My app takes some time to load, but with some patience, it can generate some entries that really sound like me! 
Check it out here - https://diary-khmwtmm5lq-uc.a.run.app/
