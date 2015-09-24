Hostapd Enhanced MANA
================
The project is forked from hostapd MANA whose authors are Dominic White (singe) & Ian de Villiers @ sensepost (research@sensepost.com). The original readme.md file is attached right after this disclamier and introduction. Meanwhile, all patch files, including the original ones from Dominic White (singe) & Ian de Villiers, are licensed under a Creative Commons Attribution-ShareAlike 4.0 International License (http://creativecommons.org/licenses/by-sa/4.0/). Hostapd's code retains it's original license available in COPYING.

Disclaimer
--------
The information in this repository is only for academic purpose and a prototype for the research paper submitted to a security proceeding. Any actions and or activities related to the material contained within this repository is solely your responsibility. The misuse of the information in this repository can result in criminal charges brought against the persons in question. The authors and the Hong Kong Polytechnic Univerisity will not be held responsible in the event any criminal charges be brought against any individuals misusing the information in this repository to break the law.

免责声明
--------
本网站提供的程序可能带有攻击性，仅供安全研究与学术论文原型之用，用户将其信息做其他用途，由用户承担全部法律及连带责任，本人与香港理工大学不承担任何法律及连带责任。



hostapd MANA
================
by Dominic White (singe) & Ian de Villiers @ sensepost (research@sensepost.com)

Overview
--------
A access point (evilAP) first presented at Defcon 22.

More specifically, it contains the improvements to KARMA attacks we implemented into hostapd, as well as the ability to rogue EAP access points.

This will track the hostapd releases, although at a somewhat lagged pace depending on time. At the time of publication this was up to date with the latest hostapd-2.3 branch.

Contents
--------

It contains:
* hostapd-mana - modified hostapd that implements our new karma attacks
* crackapd - a tool for offloading the cracking of EAP creds to an external tool and re-adding them to the hostapd EAP config (auto crack 'n add)

Installation
------------

The build instructions are exactly the same as hostapd's, and can be found in hostapd/README

Pre-Requisites
--------------

_Hardware_

You'll need a wifi card that supports master mode. You can check whether it does by running:
    iw list
You want to see "AP" in the output. Something like:
```
Supported interface modes:
         * IBSS
         * managed
         * AP
         * AP/VLAN
         * monitor
         * mesh point
```
More information at https://help.ubuntu.com/community/WifiDocs/MasterMode#Test_an_adapter_for_.22master_mode.22

Three cards that have been confirmed to work well, in order of preference are:
* Ubiquiti SR-71 (not made anymore :(, chipset AR9170, driver carl9170 http://wireless.kernel.org/en/users/Drivers/carl9170 ) 
* Alfa Black AWUS036NHA (chipset Atheros AR9271, buy at http://store.rokland.com/products/alfa-awus036nha-802-11n-wireless-n-usb-wi-fi-adapter-2-watt ) 
* TP-Link TL-WN722N (chipset Atheros AR9271 )

Note, the silver Alfa does not support master mode and will not work.

Running
-------

You'll need to generate a valid configuration file. Some example of these are included in the MANA toolkit at https://github.com/sensepost/mana

License
-------

The patches included in hostapd-mana by SensePost are licensed under a Creative Commons Attribution-ShareAlike 4.0 International License (http://creativecommons.org/licenses/by-sa/4.0/) Permissions beyond the scope of this license may be available at http://sensepost.com/contact us/. hostapd's code retains it's original license available in COPYING.

