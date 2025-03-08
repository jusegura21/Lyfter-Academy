list_of_departments=['Quality','Production','SHE']
site_heads={'Quality':'Jessica Smith','Engineering':'John Snow','Maintenance':'Phillipe Sparragow','Facilities':'Robert Tiimo','Production':'August Benjamin','SHE':'Mikaela Jr'}
print(list_of_departments)
print(site_heads)
for index in list_of_departments:
    site_heads.pop(index)
    print('Deleting value',index)
print("The new dictionary is")
print(site_heads)