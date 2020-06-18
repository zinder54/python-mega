from flask import Flask, render_template
import folium

app =Flask(__name__) #creates the app

@app.route('/portfolio/bokeh-chart')
def portfolio():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import show,figure, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN
    start=datetime.datetime(2019,3,10)
    end=datetime.datetime(2019,5,10)
    df = data.DataReader(name="AMZN",data_source="yahoo",start=start,end=end)

    #date_increase=df.index[df.Close > df.Open]
    #date_decrease=df.index[df.Close < df.Open]
    def inc_dec(c,o):
        if c > o:
            value="increase"
        elif c < o:
            value="decrease"
        else:
            value="equal"
        return value
    df["status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]

    df["middle"]=(df.Open+df.Close)/2
    df["height"]=abs(df.Open-df.Close)

    p=figure(x_axis_type='datetime',height=400,width=800)
    p.title.text="CandleStick Chart"
    p.grid.grid_line_alpha=0.3

    hours_12=12*60*60*1000

    p.segment(df.index,df.High,df.index,df.Low,line_color="black")

    p.rect(df.index[df.status == "increase"],df.middle[df.status == "increase"],
           hours_12,df.height[df.status=="increase"],fill_color="#90EE90",line_color="black")
    p.rect(df.index[df.status =="decrease"],df.middle[df.status == "decrease"],
           hours_12,df.height[df.status=="decrease"],fill_color="#CD5C5C",line_color="black")
    script1, div1, = components(p)
    cdn_js=CDN.js_files[0]
    return render_template("portfolio-details.html",script1=script1,div1=div1,cdn_js=cdn_js)


@app.route('/') ##creates the page and its location
def home():#creates function for said page
    return render_template("index.html")##renders the page and points to html in templates folder

@app.route('/portfolio/folium-map') ##same as above but for about
def about():
    return render_template("folium-map.html")

@app.route('/plot')
def plot():
     return render_template('portfolio-details.html')

if __name__ =="__main__": ##creates an if statement so this csnnot be imported otherwise it will
##be runnin on multiple servers
    app.run(debug=True)##runs the app
