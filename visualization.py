from models import engine
import pandas
import matplotlib.pyplot as plt

def show(now):
    df = pandas.read_sql("SELECT user, push_count FROM pushes", engine)
    df.plot(kind="bar", x="user", y="push_count", title='Relación developer/push', sort_columns="True", color=['#f3836b'])
    plt.savefig('static/images/'+now+'.jpg')


