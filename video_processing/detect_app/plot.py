from app import df
from bokeh.plotting import figure,show,output_file
from bokeh.models import HoverTool, ColumnDataSource

df["start_string"]=df["start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["end_string"]=df["start"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

p=figure(x_axis_type="datetime",plot_height=100,plot_width=500,sizing_mode="scale_both",title="motion graph")
p.yaxis.minor_tick_line_color=None
p.yaxis[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("start","@start_string"),("end","@end_string")])
p.add_tools(hover)


q=p.quad(left="start",right="end",bottom=0,top=1,color="green",source=cds)


output_file("m_graph.html")
show(p)
