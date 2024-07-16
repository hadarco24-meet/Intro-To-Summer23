from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return '''<html> 
    <h1> Welcome to our gallery!</h1>
    <h2>in the gallery tou can find three types of photos: food, pets, and outer space.</h2>
    <a href="/food1">click here to go the first food picture</a>
    <br></br>
    <a href="/pet2">click here to go the second pet picture</a>
    <br></br>
    <a href="/space1">click here to go the first space picture</a>
    </html>'''

@app.route("/food1")
def food1():
    return '''<html>
    <h1>welcome to the first food picture!</h1>
    <br></br>
    <img src="https://media-cdn.tripadvisor.com/media/photo-s/05/b0/2a/7c/sushi-bar-jerusalem.jpg">
    <br></br>
    <a href="/home">click here to go home</a>
    <br></br>
    <a href="/food2">click here to go the second food picture</a>
    </html>'''

@app.route("/food2")
def food2():
    return '''<html>
    <h1>welcome to the second food picture!</h1>
    <br></br>
    <img src="https://www.southernliving.com/thmb/3x3cJaiOvQ8-3YxtMQX0vvh1hQw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/2652401_QFSSL_SupremePizza_00072-d910a935ba7d448e8c7545a963ed7101.jpg">
    <br></br>
    <a href="/food1">click here to go the first food picture</a>
    <br></br>
    <a href="/food3">click here to go the third food picture</a>

    </html>'''

@app.route("/food3")
def food3():
    return '''<html>
    <h1>welcome to the third food picture!</h1>
    <br></br>
    <img src="https://www.thespruceeats.com/thmb/ed2I1ndnNKkZ4khwdC351qvLtSM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/slow-cooker-hamburgers-recipe-for-kids-2098104-hero-01-3dd9bf2b2ca748358047f2ff4e73b64c.jpg">
    <br></br>
    <a href="/home">click here to go home</a>
    <br></br>
    <a href="/food2">click here to go the second food picture</a>
    </html>'''

@app.route("/pet2")
def pet2():
    return '''<html>
    <h1>welcome to the second pet picture!</h1>
    <br></br>
    <img src="https://www.dogster.com/wp-content/uploads/2024/02/four-chow-chow-puppies-in-the-studio_Waldemar-Dabrowski_Shutterstock.jpg">
    <br></br>
    <a href="/pet3">click here to go the third pet picture</a>
    <br></br>
    <a href="/pet1">click here to go the first pet picture</a>
    <br></br>
    <a href="/home">click here to go home</a>
    </html>'''

@app.route("/pet1")
def pet1():
    return '''<html>
    <h1>welcome to the first pet picture!</h1>
    <br></br>
    <img src="https://d128mjo55rz53e.cloudfront.net/media/images/blog-breed-golden_retriever_2.max-400x400.format-jpeg.jpg">
    <br></br>
    <a href="/pet2">click here to go the second pet picture</a>
    </html>'''

@app.route("/pet3")
def pet3():
    return '''<html>
    <h1>welcome to the third pet picture!</h1>
    <br></br>
    <img src="https://i.natgeofe.com/n/9135ca87-0115-4a22-8caf-d1bdef97a814/75552.jpg">
    <br></br>
    <a href="/pet2">click here to go the second pet picture</a>
    </html>'''

@app.route("/space1")
def space1():
    return '''<html>
    <h1>welcome to the first space picture!</h1>
    <br></br>
    <img src="https://cdn.wccftech.com/wp-content/uploads/2016/09/spacee-scaled.jpg">
    <br></br>
    <a href="/space2">click here to go the second space picture</a>
    <br></br>
    <a href="/space3">click here to go the third space picture</a>
    <br></br>
    <a href="/home">click here to go home</a>
    </html>''' 

@app.route("/space2")
def space2():
    return '''<html>
    <h1>welcome to the second space picture!</h1>
    <br></br>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSva80qn921XF6JDyEMAvAcAibZTDL4nIuOdA&s">
    <br></br>
    <a href="/space1">click here to go the first space picture</a>
    <br></br>
    <a href="/space3">click here to go the third space picture</a>
    </html>'''

@app.route("/space3")
def space3():
    return '''<html>
    <h1>welcome to the third space picture!</h1>
    <br></br>
    <img src="https://e3.365dm.com/23/09/768x432/skynews-milky-way-galaxy_6293650.jpg?20230922100022">
    <br></br>
    <a href="/space1">click here to go the first space picture</a>
    <br></br>
    <a href="/space2">click here to go the second space picture</a>
    </html>'''

if __name__ == '__main__':
    app.run(debug=True)


    







