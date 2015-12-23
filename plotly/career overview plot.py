
# coding: utf-8

# In[ ]:

import plotly.offline as pl
import pandas as pd
import colorlover as cl
import numpy as np
from plotly.graph_objs import *
pl.init_notebook_mode() 


# In[1]:

{'year' : range(2005,2018),
'Statistics' : [None,None,None,None,5,35,51,65,83,95,100,103,105,109,112],
'Programming' : [15,20,22,35,50,63,69,75,88,93,92,94,95,99],
'Business Intelligence' :[None,None,None,None,None,None,None,5,20,43,60,71,75,82],
'Being a nerd':[68,70,75,80,82,87,85,90,88,89,87,90,92,95]
}


# In[ ]:

df = df.sort(['interest level'], ascending=[1])
#df['interest level'] = np.round(df['interest level'] /2)
df.head()


# In[ ]:

def myBar(category):
     c = it.next()
     df_s = df.loc[df['category'] == category].sort(['interest level'], ascending=[1])
     
     return [Bar(
            name="{}".format(category),
            y=df_s["name"],
            x=df_s["experience level"],
            orientation='h',
            legendgroup="Experience",
            yaxis="y",
            xaxis="x1",
            marker=Marker(
                color=c[5]        # set bar colors
                
        )
            
        ),        Bar(
            name="Interest - {}".format(category),
            y=df_s["name"],
            x=df_s["interest level"],
            orientation='h',
            legendgroup="Interest",
            showlegend=False,
            yaxis="y",
            xaxis="x2",
            marker=Marker(
                color=c[6]        # set bar colors
                )
        )]

def make_annotation(x, y):
        return Annotation(
        text="{:2.0f}".format(abs(x)),     # text is the y-coord
        showarrow=False, # annotation w/o arrows, default is True
        x=abs(x),               # set x position
        xref='x1' if x<0 else 'x2',          # position text horizontally with x-coords
        xanchor='left' if x<0 else 'right',  # x position corresp. to center of text
        yref='y',            # set y position 
        yanchor='center',       # position text vertically with y-coords
        y=y,                 # y position corresp. to top of text
        font=Font(
            color='#ccc',  # set font color
            size=11           #   and size   
        )
    )

def anno1(s, x):
    return Annotation(
        text=s,     # text is the y-coord
        showarrow=False, # annotation w/o arrows, default is True
        x=x,               # set x position
        xref='x',          # position text horizontally with x-coords
        xanchor='center',  # x position corresp. to center of text
        yref='paper',            # set y position 
        yanchor='top',       # position text vertically with y-coords
        y=-0.05,                 # y position corresp. to top of text
        font=Font(
            color='#000',  # set font color
            size=11           #   and size   
        ),      
        bgcolor='#F5F3F2', # light grey background color
        borderpad=10       # set border/text space (in pixels)
)


# In[181]:

values = cl.scales['7']['seq']
it = iter([values[k] for k in ['BuGn', 'PuBu', 'Purples']])


annotations = Annotations([make_annotation(-x, y) for x, y in zip(df["experience level"], df["name"])]+
                         [make_annotation(x, y) for x, y in zip(df["interest level"], df["name"])])



fig = Figure(
    data=Data(myBar('Food and beverages') + myBar('Hobby') + myBar('Professional')
                                
    ),
    layout=Layout(
        title='Jos Polfliet - skills',
        barmode='overlay',
        autosize=False,   # (!) turn off autosize 
        height=500,       # plot's height and
        width=750,  
        xaxis1=XAxis(
            title="Experience",
            anchor='y1',
            domain=[0.0, 0.5],
            zeroline=False,
            autorange='reversed'
        ),
        xaxis2=XAxis(
            title="Interest",
            anchor='free',
            domain=[0.5, 1.0],
            position=0.0,
            zeroline=False,
        ),
        yaxis=YAxis(
            anchor='x1',
            domain=[0.0, 1.0]
        ),
        annotations=annotations,
        margin=Margin(
            l=150,        
        ),
    ),
       )
pl.iplot(fig)


# In[173]:

fig = plotly.tools.make_subplots(
    rows=1,
    cols=2,
    shared_yaxes=True
)
print fig.to_string()

