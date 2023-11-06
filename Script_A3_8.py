from pathlib import Path
import ifcopenshell
import xlsxwriter


modelname = "SKYLAB_fixed"

try:
    dir_path = Path(__file__).parent
    model_url = Path.joinpath(dir_path, 'model', modelname).with_suffix('.ifc')
    model = ifcopenshell.open(model_url)
except OSError:
    try:
        import bpy
        model_url = Path.joinpath(Path(bpy.context.space_data.text.filepath).parent, 'model', modelname).with_suffix('.ifc')
        model = ifcopenshell.open(model_url)
    except OSError:
        print(f"ERROR: please check your model folder : {model_url} does not exist")


number_type = 0
number_door = 0 
total_area = 0.0
workbook1 = xlsxwriter.Workbook('Output_file_1_Errors.xlsx')
workbook2 = xlsxwriter.Workbook('Output_file_2_LCAbyg.xlsx')
worksheet1 = workbook1.add_worksheet()
worksheet2 = workbook2.add_worksheet()
bold1 = workbook1.add_format({'bold': True})
bold2 = workbook2.add_format({'bold': True})
count_pairs = 0
door_index_list=[]
door_height_list=[]
door_width_list=[]
door_number = 0 
door_area_list=[]   
identical_pairs_count={}  
minimal_door_size = 1.8 #m²
   
for door in model.by_type("IfcDoor"):
    door_height = float(format((door.OverallHeight) * 0.001,".2f"))
    door_height_list. append(door_height)
    door_width = float(format((door.OverallWidth) * 0.001,".2f"))
    door_width_list. append(door_width)
    door_area = float(format((door.OverallHeight) * (door.OverallWidth) * 0.000001,".2f"))   
    door_area_list.append(door_area)
    door_number= door_number+1
    door_index_list. append(door_number) 
      
material=[]
material_constituent_1 = []
material_constituent_2 =[]
        
for door in model.by_type("IfcDoor"):
    if door.HasAssociations:
        for i in door.HasAssociations:
            if i.is_a('IfcRelAssociatesMaterial'):
                if i.RelatingMaterial.is_a('IfcMaterial'):
                    material.append(i.RelatingMaterial.Name)
                else: 
                    material.append("" "")
                  
                if i.RelatingMaterial.is_a('IfcMaterialConstituentSet'):
                    j = 0        
                    for materials in i.RelatingMaterial.MaterialConstituents:  
                        if j == 0: 
                            material_constituent_1.append(materials.Name)
                        if j ==1: 
                            material_constituent_2.append(materials.Name)
                            
                        j = j +1            
                else: 
                    material_constituent_1.append("")
                    material_constituent_2.append("")
i = 0 
material_list = []
while i < len (door_index_list):
    if material[i] != "":
        material_list.append(material[i])
    else:
        if material_constituent_1[i]!= "<Unnamed>": 
            material_list.append(material_constituent_1[i])
        else: 
            material_list.append(material_constituent_2[i])
    i+=1
i = 0
worksheet2.write(0,0,'Full list of every door in the IFC-file' ,bold2)
worksheet2.write(1,0,"Index",bold2)
worksheet2.write(1,1,"Height [m]",bold2)
worksheet2.write(1,2,"Width [m]",bold2)
worksheet2.write(1,3,"Area [m2]",bold2)
worksheet2.write(1,4," Material ",bold2)
worksheet2.write(1,5,"Notes",bold2)
worksheet2.write(0,9,'Summary of types of doors according to size and material' ,bold2)
worksheet2.write(1,9,"Type number",bold2)
worksheet2.write(1,10,"Height [m]",bold2)
worksheet2.write(1,11,"Width [m]",bold2)
worksheet2.write(1,12,"Area [m2]",bold2)
worksheet2.write(1,13," Material ",bold2)
worksheet2.write(1,14,'Times occured',bold2)
a=2

while i < len(door_index_list):
    print(f"i: {i}, Door Index: {door_index_list[i]}, Height: {door_height_list[i]}, Material: {material_list[i]}")
    worksheet2.write(a,0,door_index_list[i])    
    worksheet2.write(a,1,door_height_list[i])
    worksheet2.write(a,2,door_width_list[i])
    worksheet2.write(a,3,door_area_list[i])
    worksheet2.write(a,4,material_list[i])
    if material_list[i] == "<Unnamed>" or door_area_list[i] < minimal_door_size:
        worksheet2.write(a,5,"Check the error file for this door")
    i+=1
    a+=1 
i=0

while i < len(door_index_list):
    
    pair_list = (door_height_list[i],door_width_list[i],door_area_list[i],material_list[i])
    print(pair_list)
    if pair_list in identical_pairs_count:
        identical_pairs_count[pair_list] += 1
    else:
        identical_pairs_count[pair_list] = 1
    i+=1
    
print(identical_pairs_count)
a=2
      
for pair_list, count in identical_pairs_count.items():
    if count >= 1 :
        number_type += 1
        print("Door type", number_type, "with size", pair_list[0],"x",pair_list[1],f" m occurred {count} time(s), these doors have an area of",pair_list[2],"m²")

        worksheet2.write(a,9,number_type)
        worksheet2.write(a,10,float(pair_list[0]))
        worksheet2.write(a,11,float(pair_list[1]))
        worksheet2.write(a,12,float(pair_list[2]))
        worksheet2.write(a,13,(pair_list[3]))
        worksheet2.write(a,14,count)
        a+=1

        print ("---------------------------------------------------------------------------------------------------")

workbook2.close()

worksheet1.write(0,0,"The following doors have an error which might affect the outcome of the LCA calculations",bold1)
worksheet1.write(1,0,"Index",bold1)
worksheet1.write(1,1,"Area[m²]",bold1)
worksheet1.write(1,2,"Material",bold1)
worksheet1.write(1,3,"Problem",bold1)
a=2
i=0

while i < len(door_index_list):
    if material_list[i] == "<Unnamed>":
        worksheet1.write(a,0,door_index_list[i]) 
        worksheet1.write(a,1,door_area_list[i])
        worksheet1.write(a,2,material_list[i])
        worksheet1.write(a,3,"This door doesn't have any material assigned according to the IFC-file")
        a+=1
        i+=1
    elif door_area_list[i] < minimal_door_size:
        worksheet1.write(a,0,door_index_list[i]) 
        worksheet1.write(a,1,door_area_list[i])
        worksheet1.write(a,2,material_list[i])
        worksheet1.write(a,3,"This door has an area which is smaller than 1,8 m²")
        a+=1
        i+=1
    else:
        i+=1    
workbook1.close()













