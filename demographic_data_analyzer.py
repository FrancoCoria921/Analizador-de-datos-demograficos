import pandas as pd
import numpy as np

def calculate_demographic_data():
    # Leer los datos
    df = pd.read_csv('adult.data.csv')
    
    # 1. ¿Cuántas personas de cada raza?
    race_count = df['race'].value_counts()
    
    # 2. Edad promedio de los hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # 3. Porcentaje de personas con licenciatura
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)
    
    # 4. Porcentaje de educación avanzada que gana >50K
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    
    higher_education_rich = round(
        (higher_education['salary'] == '>50K').sum() / len(higher_education) * 100, 1
    )
    
    # 5. Porcentaje de sin educación avanzada que gana >50K
    lower_education_rich = round(
        (lower_education['salary'] == '>50K').sum() / len(lower_education) * 100, 1
    )
    
    # 6. Mínimo de horas trabajadas por semana
    min_work_hours = df['hours-per-week'].min()
    
    # 7. Porcentaje que trabaja mínimo horas y gana >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').sum() / len(num_min_workers) * 100, 1
    )
    
    # 8. País con mayor porcentaje de >50K
    country_stats = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)
    
    # 9. Ocupación más popular para >50K en India
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_earners['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Para probar localmente
if __name__ == '__main__':
    result = calculate_demographic_data()
    for key, value in result.items():
        print(f"{key}: {value}")