import graph

title = 'ConvLayers with LaplacianMatrix'

graph.draw_1figure(train_loss_list, title+': Loss')
graph.draw_1figure(train_loss_list_each_square, title+': LossForEachSquare', y_tickLimit=5)
graph.draw_2figures(train_acc_list, test_acc_list, 'Accuarcy of TrainData', 'Accuracy of TestData', title+': Accuracy')
