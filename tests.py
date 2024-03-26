# HERE-6
_fx_ = dict(
  dev =      'cuda',     
  ctr =  True      ,    # False,
  mdp =  True      ,
  prc =     'pomdp',    # obe decide
  stM =   6e7      ,    # 6e7
  stp =    64      ,    # ARES 256 test on vscode; 384,512~30000
  rll =     2      ,    # ARES 2(check) 3(half) 4(use)
  Ldec= False      ,
  dec = 'cub'      ,
  sNh =    31      ,
  ren = False      ,
  lyr =     1      ,
  epi = 30000      ,    # 30000 Datasets
  Iva =    10      ,    # Eval HERE-2
  Ilo =     5      ,    # Filelogs    0 if False
  Isa =    10      ,    # save partial
  pop = False      ,
  nrm =    10.0    ,
  lim =  True      ,
  gmm =     0.9375 ,
  gae =     0.5    ,
  inp =    36      , 
  oup =     2      ,
  shr = False      ,
  hst = 'localhost')

TFC_ARG =[['--fLdec' , False      , [ 'true']  ], 
          ['--fSren' , False      , [ 'true']  ],
          ['--f_shr' , False      , [ 'true']  ],
          ['--f_log' ,bool(_fx_['Ilo']), [ 'true']  ],
          ['--f_sav' ,bool(_fx_['Isa']), [ 'true']  ],    # save partial
          ['--f_val' ,bool(_fx_['Iva']), [ 'true']  ],    # eval cfg['fWmod'] decide FIXME VAL X2
          ['--f_pop' , False      , [ 'true']  ],
          ['--fTlim' ,  True      , ['false']  ],
          ['--fEctr' ,  True      , ['false']  ],    # False,
          ['--f_mdp' ,  True      , ['false']  ],
          ['--fVnrm' ,  True      , ['false']  ],
          ['--f_gae' ,  True      , ['false']  ],
          ['--f_dec' ,       'cub',   str      ],
          ['--f_dmm' ,      'cuda',   str      ],  
          ['--f_prc' ,     'pomdp',   str      ],    # obe decide
          ['--l_hst' , _fx_['hst'],   str      ],
          ['--qΛstp' , _fx_['stM'],   int      ],    # 6e7
          ['--qVstp' , _fx_['stp'],   int      ],    # 30000
          ['--qMepi' , _fx_['epi'],   int      ],    # 30000 Datasets
          ['--zIval' , _fx_['Iva'],   int      ],    # Internal for eval
          ['--zIlog' , _fx_['Ilo'],   int      ],    # Internal for logs
          ['--zIsav' , _fx_['Isa'],   int      ],    # Internal for save
          ['--qHsiz' , _fx_['sNh'],   int      ],
          ['--q_onp' , _fx_['inp'],   int      ],
          ['--q_rll' , _fx_['rll'],   int      ],    # 10: 10 # HERE-7
          ['--qVrll' , _fx_['rll'],   int      ],
          ['--qRlyr' ,     1      ,   int      ],
          ['--q_iup' ,     2      ,   int      ],
          ['--gMnrm' , _fx_['nrm'], float      ],
          ['--z_gae' , _fx_['gae'], float      ],
          ['--z_gmm' ,     0.9375 , float      ]]

# TODO
def getrArg( fc='n'):
    return  TFC_ARG