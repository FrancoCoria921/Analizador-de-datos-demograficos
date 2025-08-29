from demographic_data_analyzer import calculate_demographic_data

def test_demographic_data():
    result = calculate_demographic_data()
    
    print("=== RESULTADOS DEL ANÁLISIS DEMOGRÁFICO ===\n")
    
    print(f"1. Distribución por raza:")
    print(result['race_count'])
    print(f"\n2. Edad promedio de hombres: {result['average_age_men']}")
    print(f"3. Porcentaje con licenciatura: {result['percentage_bachelors']}%")
    print(f"4. Educación avanzada que gana >50K: {result['higher_education_rich']}%")
    print(f"5. Sin educación avanzada que gana >50K: {result['lower_education_rich']}%")
    print(f"6. Mínimo horas trabajadas: {result['min_work_hours']}")
    print(f"7. Porcentaje con mínimo horas que gana >50K: {result['rich_percentage']}%")
    print(f"8. País con mayor % de >50K: {result['highest_earning_country']} ({result['highest_earning_country_percentage']}%)")
    print(f"9. Ocupación más popular en India para >50K: {result['top_IN_occupation']}")

if __name__ == '__main__':
    test_demographic_data()