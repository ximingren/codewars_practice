from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier, GBTClassifier, MultilayerPerceptronClassifier, LinearSVC
from pyspark.ml.feature import StringIndexer,VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.shell import spark

data=spark.read.format('libsvm').load('/media/four/four/spark-2.2.0-bin-hadoop2.7/data/mllib/sample_libsvm_data.txt')
# labelIndexer=StringIndexer(inputCol='label',outputCol='indexedLabel').fit(data)
# featureIndexer=VectorIndexer(inputCol='features',outputCol='indexedFeatures',maxCategories=4).fit(data)
# print(data)
# print(labelIndexer)

# data=spark.read.format('libsvm').load('/media/four/four/spark-2.2.0-bin-hadoop2.7/data/mllib/sample_libsvm_data.txt')
# labelIndexer=StringIndexer(inputCol='label',outputCol='indexedLabel').fit(data)
# featureIndexer=VectorIndexer(inputCol='features',outputCol='indexedFeatures',maxCategories=4).fit(data)
# (trainingData,testData)=data.randomSplit([0.7,0.3])
# gbt=GBTClassifier(labelCol='indexedLabel',featuresCol='indexedFeatures',maxIter=10)
# pipeline=Pipeline(labelIndexer,featureIndexer,gbt)
# model=pipeline.fit(trainingData)
# predictions=model.transform(testData)
# print(predictions)
#
# data=spark.read.format('libsvm').load('/media/four/four/spark-2.2.0-bin-hadoop2.7/data/mllib/sample_multiclass_classification_data.txt')
# print(data.show())
# splits=data.randomSplit([0.6,0.4],1234)
# train=splits[0]
# test=splits[1]
# layers=[4,5,4,3]
# trainer=MultilayerPerceptronClassifier(maxIter=100,layers=layers,blockSize=128,seed=1234)
# model=trainer.fit(train)
# result=model.transform(test)
# print (result)

# lsvc=LinearSVC(maxIter=10,regParam=0.1)
# lsvcModel=lsvc.fit(data)

from pyspark.ml.linalg import Vectors
from pyspark.ml.stat import Correlation
data=[(Vectors.sparse(4,[(0,1.0),(3,-2.0)]),),
       (Vectors.dense([4.0,5.0,0.0,3.0]),),
      (Vectors.dense([6.0,7.0,0.0,8.0]),),
      (Vectors.sparse(4,[(0,9.0),(3,1.0)]),)]
df=spark.createDataFrame(data,['features'])
r1=Correlation.corr(df,'features','spearman')
print(r1.head())