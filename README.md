
<br />
<div align="center">
<h3 align="center">41934 Advanced Building Information Modeling (BIM)</h3>
  <p align="center">
    Assignment 03
    <p align="center">
    12th November 202
    <br />
</div>


# Table of Contents
1. [Creators](#creators)
2. [3A: Analyse use case](#3a-analyse-use-case)
3. [3B: Propose a (design for a) tool / workflow](#3b-propose-a-design-for-a-tool--workflow)
4. [3D: Value What is the potential improvement offered by this tool?](#3d-value-what-is-the-potential-improvement-offered-by-this-tool)


<!-- CREATORS -->
## Creators
- Naja Johansen, s184525
- Zoyan Vangenechten, s232094
- Laura Iglesias Castro, s230383


<!-- 3A: Analyse use case -->
## 3A: Analyse use case 
The aim of our project is to create a workflow that extracts the necesary information of an IFC file in order to perform a life cycle analysis (LCA) of a buidling and at the same time analyze whether there are errors or unrealistic data in the model and clarify this for the user of this tool. An LCA calculation has become an essential tool in the construction industry, and in Denmark, it is mandatory to perform an LCA calculation for new buildings. However, there are several companies that perform LCAs anyway for internal use or for branding purposes. In Denmark, the most common LCA tool used for the building industry is LCAbyg. This use case is therefore intended for all companies that need to perform an LCA in the construction industry. Our tool is intended to be use by sustainability experterts, in charge of carrying LCA of buidlings. To conduct a comprehensive LCA, one needs to have knowledge of the total building area, all materials used, and their respective quantities. Additionally, information about the building's energy consumption and product specific EDP’s are also required. 

The diagram below (Diagram 1) illustrates the various steps associated with an IFC file and how to perform a life cycle assessment (LCA). This diagram were also presented in the previous assigment as the overall purpose remains the same.


![Diagram01](Diagram1.png "Diagram 1")


The main purpose of this tool is to be used by an LCAbyg user in the industry to save time on current processes. In the existing practices, users typically have to manually extract extensive quantity schedules from the model or analyze building drawings manually. The user will utilize this tool as a kind of plug-in to analyze an IFC model automatically.

By using this tool, the following outputs are obtained:

- An overview of all building components with their dimensions, quantities, and materials. This will be organized in a way that can be easily used by the user to input the content into LCAbyg.
- An overview of building components that either lack a material or have unrealistic dimensions. This allows the user to quickly and easily identify which specific building components need to be re-modeled or further investigated. In addition, the tool will highlight any errors or unrealistic modeling choices made during the modeling phase. As a result, the tool's user will save time by receiving this summary sheet and will also know exactly where to update or account for errors in the model. Additionally, the user will also have the convenience of easily forwarding this overview to the person responsible for the model if the user is not directly involved in modeling activities.



<!-- 3B: Propose a (design for a) tool / workflow -->
## 3B: Propose a (design for a) tool / workflow
As a scope of our project, the group has been solely on gathering data related to the "doors" category (materials and quantities) using the IFC model of the Skylab building at DTU campus. Diagram 2 below illustrates the proof of concept that was performed in this use case. The diagram only describes the workflow we followed to gather dimensions and material data for the doors category. 


The group's script generates two Excel sheets as output. The first Excel sheet, “Output_file_1_Errors,” is a direct output that summarizes all the doors in the building with divergent values. This can be caused by the IFC-file, and this first output makes it easy to identify potential issues for future LCA (Life Cycle Assessment) calculations. There are two possible ways in which a door can receive an error. This is based on "rules" made by the group: either the area of the door is lower than 1.8m², or the file does not provide any material information for the door. The output also indicates which of these errors has been assigned to a specific door. In the "Output_file_1_Errors," you can clearly see where there may be problems for future LCA calculations. This detailed breakdown ensures that you can address issues promptly, ensuring the accuracy of your assessments.


The second output Excel file contains the necessary data required for LCA calculations in the software “LCAbyg.” This file not only provides essential data but also offers a summarized list of all the doors, neatly categorized by similar size and materials. Each door or door type is associated with its corresponding area, width, height, material, and, in the case of door types, the number of repetitions in the IFC-file.
This Excel file streamlines the process of performing LCA calculations, making it user-friendly and efficient. It not only assists in individual assessments but also offers a comprehensive overview/summary of the building's components, which can be invaluable during project meetings and decision-making processes. Its organized format enhances collaboration and ensures that all stakeholders have the information they need at their fingertips.
These outputs are essential tools for architects, engineers, and sustainability professionals to make informed decisions about building design and materials, ultimately contributing to a more sustainable and environmentally-conscious construction process.


![Diagram02](Diagram2.png "Diagram 2")

If you wish to further develop and enhance this tool in the future, it's important to consider how to identify the specific building part of the building. Currently, a specific ID number is missing, which needs to be linked to the particular building component represented in the two output files. For example if one intends to use output file 1 (represents errors) to go back into the building model and actually edit or update it, it's necessary to know the specific location, which is not currently possible.

In this use case, only properties associated with the doors have been examined. In the future, the tool will be developed further to include all building components.

<!-- 3D: Value What is the potential improvement offered by this tool? -->
## 3D: Value What is the potential improvement offered by this tool?

The goal of our tool is to create both business value and societal value. 
Nowadays, extracting the material and quantity information from an IFC file is a time-consuming process.  Moreover, it could be difficult to identify human modelling errors that could potentially affect the outcome of the LCA. Specially if the modelling work, the data extraction and the LCA study is carried out by different users with different backgrounds and skills. Besides, these steps are usually executed across different departments or organizations. This tool would allow a user lacking modelling and programming skills to identify the modelling errors that could affect the LCA. A list of these errors could be directly sent to the model creator, who should adjust the model. On the other hand, the script would allow the user to extract the necessary data to perform the LCA in a faster and easy way. Thus, the tool could improve the accuracy of the LCA and optimize current workflows, saving time and reducing the level of complexity. This could be translated into economical value but also into environmental value.  Increasing the accuracy of the LCA of a building could lead to more informed decisions regarding the reduction of the environmental impacts during de design phase. Enhancing the precision of a building's LCA has the potential to empower more informed choices in minimizing environmental impacts during the design phase.








