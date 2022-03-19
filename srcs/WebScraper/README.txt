Instruction of Web Crawler:
1. China.py: Used to gather the information about the module catalogue and stored the module information (Code, Name, Period, Level) into the database.
    --- Execute the program, all the settings are available in this program.
    --- Some administering schools don't have any modules. It's normal in this condition.
    --- Sometimes because of the network's condition, all the data need to check twice in order to avoid the information missing.
2. China_Detail.py: Used to get information according to the module code, it needs long time to execute.
    --- Execute the program, all the settings are available in this program.
    --- Due to the network condition, module catalogue needs to be checked twice in order to avoid the information missing.
    --- After checking, every missing module needs to collect again and then checked until there is no information occured. 
    --- All the missing information module's codes need to be entered manually in the get_code() function.
3. China_Module.py: Used to get information about the relationship between specified modules and courses, and store these information into the database.
    --- Execute the program, all the settings are available in this program.
    --- Due to the network condition, the program may be interrupt. If this condition occurs, re-execute the program until the program executes without any mistakes.
    --- As mentioned in the program, the FHSS's module catalogues are stored in PDF document. So before coping with the FHSS course page, the essential operations to change PDF into HTML document is highly needed.
4. China_Staff.py: Used to get information about the staff's information and store them into a folder contains the raw HTML document.
    --- Execute the program, all the settings are available in this program.
    --- In the first part, developers should check whether all the staff's information are stored in the related folder.
    --- In the second part, developers should check whether all the staff's information are written into the database.
    --- If the above goals are not achieve, the developers should deleted all the staff information gathered before and re-run the program.
5. China_Course_Detail.py: Used to get information about the course introduction. The source files are stored in the specified folder.
    --- Execute the program, all the settings are available in this program.
    --- The final result depends on the execution of China_Module.py. All the information originates from the information stored in the raw HTML documents collected by that program.
    --- It doesn't need to be checked twice. If there are mistakes, it must be in the China_Module.py faults.
6. ImportVue.py: Used to write the information into the front pages.
    --- Execute the program, all the settings are available in this program.
    --- Some Vue files needs further operations. In order to check the single quote and other illegal characters.
    --- Some Vue files doesnt have matched links about the module convener because the staff's name is not in available forms. It should be ignored.