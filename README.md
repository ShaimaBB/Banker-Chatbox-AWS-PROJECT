# Banker-Chatbox-AWS-PROJECT

## 🌟 Project Summary

This project showcases a chatbot built using **Amazon Lex**, designed to handle user intents such as greeting the user, checking account balances, and transferring money. The chatbot leverages **AWS Lambda** for backend processing and integrates features like:

- **Intent Recognition**: Custom intents, such as `WelcomeIntent`, greet users and handle specific conversational needs.
- **Context Tags**: Maintain conversational memory for improved user experience.
- **Customized Fallback Responses**: Enhanced user interaction by configuring `FallbackIntent` with user-friendly variations.
- **Error Handling**: Clear fallback messages triggered when unrecognized inputs are received.

My documentation of this entire project is [here](https://github.com/ShaimaBB/Banker-Chatbox-AWS-PROJECT-/blob/0af6d9974e749d5a58cdf08dc977dc0749a1cc30/ChatBox-Aws.pdf)

## 🏗️ Architecture

The chatbot integrates multiple AWS services:
- **Amazon Lex** for natural language processing.
- **AWS Lambda** for intent fulfillment.

## 🚀 Setup Guide

### Steps
1. **Set Up Amazon Lex Bot**:
   - Create intents like `WelcomeIntent` with relevant utterances.
   - Configure fallback and response variations.

2. **Integrate AWS Lambda**:
   - Link Lambda functions to process user requests dynamically.

3. **Assign IAM Role**:
   - Attach policies such as `AmazonLexRunBotsOnly` to enable smooth operation.

4. **Test and Deploy**:
   - Test the chatbot in the Lex Console.
   - Deploy it for real-world interactions.

## 📚 Challenges
- **Error Handling**: Managing fallback responses required custom configuration to improve clarity.


## 🧑‍💻 Creators
- Shaima Bashar
- [NextWork](https://learn.nextwork.org/) Resourses
