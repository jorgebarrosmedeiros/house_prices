import pickle
import pandas as pd
import numpy as np

class preco(object):
        
	def __init__(self):
	self.__qualidade = pickle.load(open("C:/ProjetosDataScience/casetecnico/parameter/area.pkl/qualidade.pkl",'rb'))
        self.__anoconstucao = pickle.load(open("C:/ProjetosDataScience/casetecnico/parameter/area.pkl/qualidade.pkl/anoconstrucao.pkl","rb"))
        self.__banheiros = pickle.load(open("C:/ProjetosDataScience/casetecnico/parameter/area.pkl/qualidade.pkl/banheiros.pkl","rb"))
        self.__comodos =  pickle.load(open("C:/ProjetosDataScience/casetecnico/parameter/area.pkl/qualidade.pkl/comodos.pkl","rb"))
        self.__lareiras = pickle.load(open("C:/ProjetosDataScience/casetecnico/parameter/area.pkl/qualidade.pkl/lareiras.pkl","rb"))
        self.__garagem = pickle.load(open("C:/ProjetosDataScience/casetecnico/parameter/area.pkl/qualidade.pkl/garagem.pkl","rb"))
	self.__area =      pickle.load(open("C:/ProjetosDataScience/casetecnico/parameter/area.pkl", "rb"))


	def feature_selection(self, df1):

		columns = ['Area', 'Qualidade', 'AnoConstrucao','Banheiros','Comodos', 'Lareiras', 'Garagem']

		return df1[columns]


	def data_preparation(self, df2)


		#area - RobustScaler
        df2["Area"] = self.__area.fit_transform(df2[["Area"]].values)

        #qualidade - MinMaxScaler
        df2["Qualidade"] = self.__qualidade.fit_transform(df2[["Qualidade"]].values)

        #anoconstrucao - MinMaxScaler
        df2["AnoConstrucao"] = self.__anoconstucao.fit_transform(df2[["AnoConstrucao"]].values)

        #banheiros - MinMaxScaler
        df2["Banheiros"] = self.__banheiros.fit_transform(df2[["Banheiros"]].values)

        #comodos - MinMaxScaler
        df2["Comodos"] = self.__comodos.fit_transform(df2[["Comodos"]].values)

        #garagem - MinMaxScaler
        df2["Garagem"] = self.__garagem.fit_transform(df2[["Garagem"]].values)
        
        #lareiras - MinMaxScaler
        df2["Lareiras"] = self.__lareiras.fit_transform(df2[["Lareiras"]].values)

        return df2

