import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

def main():
    country_info = get_data()
    regression(country_info)
    

def get_data():
    try:
        countries_data = pd.read_csv("CO2_emission_by_countries.csv")
        # Object con los codigos de paises, el codigo sirve para acceder a la info del pais. 
        countries_code = countries_data['Code'].unique()
        country_selected = input("Ingrese el codigo del pais. ").upper()
        # Se verifica si el codigo ingresado es valido.
        if country_selected in countries_code:
            # Extraer indices entre los que se encuentra la informacion del pais
            codes = list(countries_data['Code'])
            rcodes = codes.copy()
            rcodes.reverse()
            start = codes.index(country_selected)
            end = 59620 - rcodes.index(country_selected)
            country_info = []
            for i in range(start, end, 1):
                country_info.append(countries_data.loc[i])
            country_info = pd.DataFrame(country_info, columns=countries_data.columns)
            return country_info
        else:
            raise ValueError("Invalide Code")
    except ValueError as e:
        print(e)


def regression(info):
    # Population & Year
    x = info['Year'].to_numpy().reshape(len(info), 1)
    y = info['CO2 emission (Tons)'].to_numpy().reshape(len(info), 1)
    
    rgs = LinearRegression()
    rgs.fit(x, y)
    xp = np.linspace(min(x), max(x), num=2)
    yp = rgs.coef_*xp+rgs.intercept_
    r2 = round(rgs.score(x, y), 3)
    msg = "La recta es: {}x + ({})\nR2: {}".format(round(rgs.coef_[0][0], 2), round(rgs.intercept_[0], 2), r2)
    print(msg)
    graph(x, y, xp, yp, r2)
    

def graph(x, y, xp, yp, r2):
    plt.title('CO2 emission (Tons) & Year')
    plt.xlabel('Year')
    plt.ylabel('CO2 emission (Tons)')
    plt.plot(x, y, 'bo', label="puntos")
    plt.plot(xp, yp, label="Regresion lineal", color="red")
    plt.show()


if __name__ == '__main__':
    main()