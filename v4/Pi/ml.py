import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO

import pydotplus

log = pd.read_csv("log.csv")

X = log.drop("enoughWater", axis=1)
t = log["enoughWater"]

dt = DecisionTreeClassifier(random_state=0).fit(X, y)

dot_data = StringIO()
export_graphviz(dt,
                out_file=dot_data,
                filled=True,
                rounded=True,
                feature_names=X.columns,
                special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png("dt.png")