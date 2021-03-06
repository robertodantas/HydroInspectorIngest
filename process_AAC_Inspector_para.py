# Program for pulling NWM parallel output (Beta) from NCEP's
# para NOMADS HTTP server. Data is not operational, so we will
# pull whatever is available.

# Logan Karsten 
# National Center for Atmospheric Research
# Research Applications Laboratory

import datetime
import os
import sys

# Append path to include custom libraries for this workflow
sys.path.append('/d4/karsten/NWM_INSPECTOR/inspector_processing/lib')

# Import custom libraries for this workflow
import compressMod
import inspectorMod

# Establish workflow variables
errTitle = 'Error_Process_AAC_Para_Inspector'
warningTitle = 'Warning_Process_AAC_Para_Inspector'
lockFile = '/home/karsten/tmp/Process_AAC_Para_Inspector.LOCK'
completeDir = '/d4/karsten/NWM_INSPECTOR/AAC_Para'
email = 'karsten@ucar.edu'
hoursBack = 24
hoursLag = 0
webDirTmp = '/d2/karsten/INSPECTOR_PARA_TMP'
webDirFinal = '/d2/hydroinspector_data/tmp/conus/para/analysis_assimilation'

# Get PID from this process
pid = os.getpid()

# Create lock file for this process
inspectorMod.createLock(lockFile,pid,warningTitle,email)

# Establish current date object
dNow = datetime.datetime.now()

# Loop through processing window.
for hourBack in range(hoursBack,hoursLag,-1):
	# Establish datetime objects
	dCurrent = dNow - datetime.timedelta(seconds=hourBack*3600)
	dValid = dCurrent
	dInit = dCurrent - datetime.timedelta(seconds=3*3600)


	hrStrCurrent = dCurrent.strftime('%H')
	dStr1Current = dCurrent.strftime('%Y%m%d%H')
	dStr2Current = dCurrent.strftime('%Y%m%d')

	# for each product (channel, land, etc),
   # check for complete file that indicates
   # file was sucessfully downloaded, processed, and 
   # posted to hydro-c1-web to ingest into hydroInspector.

	# Channel output
	completePath = completeDir + '/nwm.t' + hrStrCurrent + \
                  'z.analysis_assim.channel_rt.tm00.conus_' + dStr1Current + \
                  '_f000.COMPLETE'
	fileDPath = 'nwm.t' + hrStrCurrent + 'z.analysis_assim.channel_rt.tm00.conus.nc'
	fileCompress = 'nwm.' + dStr2Current + '_t' + hrStrCurrent + '_f000.analysis_assim.' + \
                  'channel_rt.conus.COMPRESS.nc'
	httpDir = 'http://para.nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/para/nwm.' + dStr2Current + \
             '/analysis_assim/'
	if not os.path.isfile(completePath):
		findStatus = inspectorMod.downloadNwmHTTP(httpDir,completeDir,fileDPath,fileCompress,errTitle,email,lockFile)
		if findStatus == 1:
			inspectorMod.copyToWeb(completeDir + '/' + fileCompress,webDirTmp,errTitle,email,lockFile)
			inspectorMod.shuffleFile(fileCompress,webDirFinal,webDirTmp,errTitle,email,lockFile)
			inspectorMod.genFlag(completePath,errTitle,email,lockFile)
			inspectorMod.checkFile(completePath,errTitle,email,lockFile)
			inspectorMod.deleteFile(completeDir + "/" + fileCompress,errTitle,email,lockFile)

	# Land output
	completePath = completeDir + '/nwm.t' + hrStrCurrent + \
                  'z.analysis_assim.land.tm00.conus_' + dStr1Current + \
                  '_f000.COMPLETE'
	fileDPath = 'nwm.t' + hrStrCurrent + 'z.analysis_assim.land.tm00.conus.nc'
	fileCompress = 'nwm.' + dStr2Current + '_t' + hrStrCurrent + '_f000.analysis_assim.' + \
                  'land.conus.COMPRESS.nc'
	httpDir = 'http://para.nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/para/nwm.' + dStr2Current + \
             '/analysis_assim/'
	if not os.path.isfile(completePath):
		findStatus = inspectorMod.downloadNwmHTTP(httpDir,completeDir,fileDPath,fileCompress,errTitle,email,lockFile)
		if findStatus == 1:
			inspectorMod.copyToWeb(completeDir + '/' + fileCompress,webDirTmp,errTitle,email,lockFile)
			inspectorMod.shuffleFile(fileCompress,webDirFinal,webDirTmp,errTitle,email,lockFile)
			inspectorMod.genFlag(completePath,errTitle,email,lockFile)
			inspectorMod.checkFile(completePath,errTitle,email,lockFile)
			inspectorMod.deleteFile(completeDir + "/" + fileCompress,errTitle,email,lockFile)

	# Terrain output
	completePath = completeDir + '/nwm.t' + hrStrCurrent + \
                  'z.analysis_assim.terrain_rt.tm00.conus_' + dStr1Current + \
                  '_f000.COMPLETE'
	fileDPath = 'nwm.t' + hrStrCurrent + 'z.analysis_assim.terrain_rt.tm00.conus.nc'
	fileCompress = 'nwm.' + dStr2Current + '_t' + hrStrCurrent + '_f000.analysis_assim.' + \
                  'terrain_rt.conus.COMPRESS.nc'
	httpDir = 'http://para.nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/para/nwm.' + dStr2Current + \
             '/analysis_assim/'
	if not os.path.isfile(completePath):
		findStatus = inspectorMod.downloadNwmHTTP(httpDir,completeDir,fileDPath,fileCompress,errTitle,email,lockFile)
		if findStatus == 1:
			inspectorMod.copyToWeb(completeDir + '/' + fileCompress,webDirTmp,errTitle,email,lockFile)
			inspectorMod.shuffleFile(fileCompress,webDirFinal,webDirTmp,errTitle,email,lockFile)
			inspectorMod.genFlag(completePath,errTitle,email,lockFile)
			inspectorMod.checkFile(completePath,errTitle,email,lockFile)
			inspectorMod.deleteFile(completeDir + "/" + fileCompress,errTitle,email,lockFile)

	# Forcing
	completePath = completeDir + '/nwm.t' + hrStrCurrent + \
                  'z.analysis_assim.fe.tm00.conus_' + dStr1Current + \
                  '_f000.COMPLETE'
	fileDPath = 'nwm.t' + hrStrCurrent + 'z.analysis_assim.forcing.tm00.conus.nc'
	fileCompress = 'nwm.' + dStr2Current + '_t' + hrStrCurrent + '_f000.fe_analysis_assim.' + \
                  'conus.COMPRESS.nc'
	httpDir = 'http://para.nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/para/nwm.' + dStr2Current + \
             '/forcing_analysis_assim/'
	if not os.path.isfile(completePath):
		findStatus = inspectorMod.downloadNwmHTTP(httpDir,completeDir,fileDPath,fileCompress,errTitle,email,lockFile)
		if findStatus == 1:
			compressMod.compressV11Forcing(completeDir + '/' + fileCompress,errTitle,email,lockFile)
			inspectorMod.copyToWeb(completeDir + '/' + fileCompress,webDirTmp,errTitle,email,lockFile)
			inspectorMod.shuffleFile(fileCompress,webDirFinal,webDirTmp,errTitle,email,lockFile)
			inspectorMod.genFlag(completePath,errTitle,email,lockFile)
			inspectorMod.checkFile(completePath,errTitle,email,lockFile)
			inspectorMod.deleteFile(completeDir + "/" + fileCompress,errTitle,email,lockFile)

# Delete lock file
inspectorMod.deleteFile(lockFile,errTitle,email,lockFile)
