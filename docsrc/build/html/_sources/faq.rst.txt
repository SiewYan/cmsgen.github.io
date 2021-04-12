FAQ
===

.. contents::
   :local:

What is the procedure used for generating Madgraph?
----------------------------------------------------------

you can find instructions on how to use the MadGraph5_aMCatNLO generator on this twiki page: ::
  
  https://twiki.cern.ch/twiki/bin/view/CMS/QuickGuideMadGraph5aMCatNLO

Note since 2018/11/28, the master branch of genproductions is merged with the *MG5_aMC@NLO v26X branch*. We instruct users to clone the whole genproductions from git and work there. On a lxplus machine (not in a release area), you can do the following: ::

  git clone https://github.com/cms-sw/genproductions.git
  #(if you need to use mg 2.4.2 then do the following git clone https://github.com/cms-sw/genproductions.git -b mg242legacy)
  cd genproductions/bin/MadGraph5_aMCatNLO/
  ./gridpack_generation.sh <name of process card without _proc_card.dat> <folder containing cards relative to current location>

Example: ::

  ./gridpack_generation.sh wplustest_4f_LO cards/examples/wplustest_4f_LO

Where can i find the Info for MC production for Ultra Legacy Campaigns 2016, 2017, 2018
----------------------------------------------------------------------------------------

Ultra legacy (UL) campaigns are displayed at this `link <https://cms-pdmv.cern.ch/mcm/campaigns?prepid=RunIISummer20UL*&page=-1&shown=63>`_ . The UL campaigns are the standard campaigns with the corresponding setup schemes to emulate the RunII datataking period. 

For more information, please visit `Monte Carlo Production tool <https://cms-pdmv.gitbook.io/project/mccontact/info-for-mc-production-for-ultra-legacy-campaigns-2016-2017-2018>`_ .
