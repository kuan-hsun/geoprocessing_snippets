import arcpy
import os

arcpy.env.overwriteOutput = True
# define local variables
wrkspc = 'D:/Project_Data/AD_web'
mxd_path = os.path.join(wrkspc, 'ADdata.mxd')
mapDoc = arcpy.mapping.MapDocument(mxd_path)

print mapDoc

con = 'GIS Servers/arcgis on localhost_6080 (admin)' #必須要用admin權限的connection
service = 'ADdata'
sddraft = wrkspc + service + '.sddraft'
sd = wrkspc + service + '.sd'
folder_name = 'AD'
summary = '建築結構資料庫查詢'
tags = '結構資料庫查詢'

# create service definition draft 產生.sd檔
analysis = arcpy.mapping.CreateMapSDDraft(mapDoc, sddraft, service, 'ARCGIS_SERVER', con, True, folder_name, summary, tags)


# Print errors, warnings, and messages returned from the analysis
print "The following information was returned during analysis of the MXD:"
for key in ('messages', 'warnings', 'errors'):
  print '----' + key.upper() + '---'
  vars = analysis[key]
  for ((message, code), layerlist) in vars.iteritems():
    print '    ', message, ' (CODE %i)' % code
    print '       applies to:',
    for layer in layerlist:
        print layer.name,


# stage and upload the service if the sddraft analysis did not contain errors
if analysis['errors'] == {}:
    # Execute StageService
    arcpy.StageService_server(sddraft, sd)
    # Execute UploadServiceDefinition
    arcpy.UploadServiceDefinition_server(sd, con)
    print "Service successfully published"
else: 
    # if the sddraft analysis contained errors, display them
    print analysis['errors']

print arcpy.GetMessages()
