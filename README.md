# Cap-Recognizer
An image classification model from data collection, cleaning, model training, deployment and API integration. <br/>
The model can classify 20 different types of caps <br/>
The types are following: <br/>
1. baseball cap
2. beanie cap
3. fedora cap
4. cowboy hat
5. kepi cap
6. flat cap
7. trucker cap
8. newsboy cap
9. pork pie hat
10. bowler hat
11. top hat
12. sun hat
13. boater hat
14. ivy cap
15. bucket hat
16. balaclava cap
17. turban cap
18. taqiyah cap
19. rasta cap
20. visor cap

# Dataset Preparation
**Data Collection:** Downloaded from DuckDuckGo using term name <br/>
**DataLoader:** Used fastai DataBlock API to set up the DataLoader. <br/>
**Data Augmentation:** fastai provides default data augmentation which operates in GPU. <br/>
Details can be found in `notebooks/data_prep.ipynb`

# Training and Data Cleaning
**Training:** Fine-tuned a resnet34 model for 5 epochs (3 times) and got upto ~89% accuracy. <br/>
**Data Cleaning:** This part took the highest time. Since I collected data from browser, there were many noises. Also, there were images that contained. I cleaned and updated data using fastai ImageClassifierCleaner. I cleaned the data each time after training or finetuning, except for the last time which was the final iteration of the model. <br/>

# Model Deployment
I deployed to model to HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [here](https://huggingface.co/spaces/fayez94/cap-recognizer_2). <br/>
<img src = "deployment/gradio_App.png" width="700" height="350">

# API integration with GitHub Pages
The deployed model API is integrated [here](https://fayez94.github.io/Cap_Recognizer/docs/cap_recognizer.html) in GitHub Pages Website. Implementation and other details can be found in `docs` folder.

## Contributions

Contributions are always welcome! If you'd like to contribute to the Cap Recognizer project, here’s how you can help:

### How to Contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add new feature'`)
5. Push to the branch (`git push origin feature-name`)
6. Open a Pull Request

### Ways You Can Contribute:
- Add support for new cap categories or labels
- Improve the accuracy of the model by fine-tuning or experimenting with new architectures
- Enhance data collection or augmentation techniques
- Update documentation or add more examples
- Report bugs or suggest new features

Thank you for considering contributing! 🙏

## 📬 Contact
For any questions or suggestions, feel free to reach out!

📧 Email: mdfayezullah2624@gmail.com  
🐙 GitHub: [fayez94](https://github.com/fayez94)
