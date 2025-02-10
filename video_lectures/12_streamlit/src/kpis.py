from read_data import read_data

df = read_data()

approved = df.query("Beslut == 'Beviljad'")
number_approved = len(approved)
total_application = len(df)
approved_percentage = f"{number_approved / total_application*100:.1f}%"

#print(approved_percentage)

def provider_kpis(provider):
    #applied = df.query(f"'Utbildningsanordnare administrativ enhet' == '{provider}'")
    applied = df.query(f"`Utbildningsanordnare administrativ enhet` == '{provider}'")
    application = len(applied)
    approved_educations = len(applied.query("Beslut == 'Beviljad'"))
    
    return application, approved_educations

print(provider_kpis('TGA Utbildning AB'))