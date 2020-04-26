########################################

import os, sys, xbmc, xbmcgui, xbmcplugin, xbmcaddon
	
#Suisse Direct By Sphinxroot QC

# Various constants used throughout the script
HANDLE = int(sys.argv[1])
ADDON = xbmcaddon.Addon(id='plugin.video.SuisseDirect')
LANGUAGE  = ADDON.getLocalizedString
THUMBNAIL_PATH = os.path.join( ADDON.getAddonInfo( 'path' ), 'resources', 'media')

def start() :

	li = xbmcgui.ListItem(label=LANGUAGE(30000), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Suisse.gif'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="plugin://plugin.video.youtube/play/?video_id=UQRDv3HtmUA", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30001), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'beatz.png'))		
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://livevideo.infomaniak.com/streaming/livecast/rp_tv_1/playlist.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30002), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'canal9.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://edge8.vedge.infomaniak.com/livecast/ik:livehd/chunklist_w1977644832.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30003), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'canalalpha.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://edge6.vedge.infomaniak.com/livecast/ik:canalalpha/chunklist_w1815884040_b2500000.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30004), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'canalalpha.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="http://canalalphaju.vedge.infomaniak.com/livecast/canalalphaju/playlist.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30005), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Couleur.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://rtsc3video-lh.akamaihd.net/i/rtsc3video_ww@513975/index_1200_av-b.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30006), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'latele.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://edge8.vedge.infomaniak.com/livecast/latele2/chunklist_w1798460365.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30007), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'lemanbleu.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://edge4.vedge.infomaniak.com/livecast/ik:naxoo/chunklist_w1332987521_b2000000.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30008), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'lfmtv.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://edge10.vedge.infomaniak.com/livecast/ik:lfmmd/chunklist_w2097806596_b3000000.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30009), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'maxtv.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://katapy.hs.llnwd.net/dieutvwza1/DIEUTVLIVE/smil:dieutv.smil/720p-playlist.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30010), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'onetv.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://edge9.vedge.infomaniak.com/livecast/ik:onefmmd/chunklist_w862344050_b3000000.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30011), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'telebasel.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://cldf-wzw-live.r53.cdn.tv1.eu/10096xtelebase/_definst_/1000199copo/live/app510394368/w162136077/live_de_1500/chunklist.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30012), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'telebielingue.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://edge3.vedge.infomaniak.com/livecast/ik:telebielinguech/chunklist_w1960722328.m3u8", listitem=li, isFolder=False)	
   	li = xbmcgui.ListItem(label=LANGUAGE(30013), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Tvm3.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://edge7.vedge.infomaniak.com/livecast/ik:tvm3/chunklist_w191085829.m3u8", listitem=li, isFolder=False)
   	li = xbmcgui.ListItem(label=LANGUAGE(30014), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Rouge.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://edge1.vedge.infomaniak.com/livecast/ik:rougetv/chunklist_w94148732.m3u8", listitem=li, isFolder=False)    
	setViewMode("500")		
	xbmcplugin.endOfDirectory( HANDLE )		
	
def setViewMode(id):
	if xbmc.getSkinDir() == "skin.confluence":
		xbmc.executebuiltin("Container.SetViewMode(" + id + ")")
			
start()