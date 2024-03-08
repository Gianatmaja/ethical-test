#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[ ]:


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        return(render_template("index.html", result = 90.23 + (-50.6 * rate)))
    else:
        return(render_template("index.html", result = "Waiting for exchange rate..."))

if __name__ == "__main__":
    app.run()


# In[ ]:




