def calculateBMI(weight, height, isMetric):
    if isMetric:
        return round(weight / height**2 * 10000.0, 2)
    else:
        return round(weight / height**2 * 703.0, 2)

def turnInputsToDic(BMI, smoke, drink, stroke, ph, mh, dw, sex, age, race, dia, phy, gen, sleep, asthma, kidney, skin):
    sample = {
        'BMI': float(BMI),
        'Smoking': smoke,
        'AlcoholDrinking': drink,
        'Stroke': stroke,
        'PhysicalHealth': float(ph),
        'MentalHealth': float(mh),
        'DiffWalking': dw,
        'Sex': sex,
        'AgeCategory': age,
        'Race': race,
        'Diabetic': dia,
        'PhysicalActivity': phy,
        'GenHealth': gen,
        'SleepTime': float(sleep),
        'Asthma': asthma,
        'KidneyDisease': kidney,
        'SkinCancer': skin
    }

