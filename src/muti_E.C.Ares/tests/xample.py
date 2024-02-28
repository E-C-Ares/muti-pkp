"""
 # calculate-uti with _np
 @ E.C.Ares
 ! MIT LICENSE
 ` analytic(纯函数) & vec-geometry(几何意义)
"""

#
from                  sqlite3 import     NotSupportedError
#import    math                      as  _mt
import          numpy                as  _np


_JB_ZeO  =    0     # 口
_JB_UeI  =    1     # 一
_JB_ReT  =  True    # 右
_JB_ЯeF  = False    # 左
_JB_NoN  =  None    # 冇
#_JB_XiS =          # 有


# constants https://standards.ieee.org/ieee/754/6210/
_ZDuPAI    =  3.141592653589793         #_np.pi
_ZDuPLI    =  1.5707963267948966        #_np.pi / 2
_ZDnPLI    =  1.5707963267948967        #_np.pi * 0.5
# constants-float
_ZDnZRO_FLT=  2.2250738585072014e-308   #_np.finfo(np.float64).tiny # 正〇
_ZD_MAX_FLT=  1.7976931e+30             #  1.7976931348623158e+30
# constants-change; {0:1, 1:2, 2:4, 3:3, 4:16, 5:10, 6:12, 7:28, 8:256, 9:360} 
_RD_CNGuPi9=  0.0174532923847436        #_np.pi /180
_RD_CNGn9iP= 57.29578                   #180    /_np.pi

# 阵囗1 EIN
_ZH_EI2    =_np.eye( 2 )
# 阵囗i GIN: GIN^N = EIN
_ZH_GI2    =_np.rot90(  _ZH_EI2) * [ +1, -1]
_ZH_RO2    = lambda  a :_ZH_EI2  *  _np.cos( a ) +  _ZH_GI2  *  _np.sin( a )
_ZH_ЯO2    = lambda  a :_ZH_EI2  *  _np.cos( a ) -  _ZH_GI2  *  _np.sin( a )

DatSelf    = lambda  a : a

_ze_ = dict(
  n  =    1.0      ,
  d  =  _RD_CNGuPi9)

_zd_ = dict(
  n  =    1.0      ,
  d  =  _RD_CNGn9iP,
  m  =    3.6      )

# 矢减标为矢变，标减标为至矢，矢减矢为中矢, 标减矢为新标
def vbb( vX, vO = 1.0): return   vX- vO
# 标加矢为标移, 矢加矢为新矢
def vdd( vX, vO = 1.0): return   vX+ vO

#def DatSelf( da      ): return  da
def Arp_De9( ld      ): return   ld*_RD_CNGuPi9  # _np.deg2rad: De9 -> Arp
def De9_Arp( ld      ): return   ld*_RD_CNGn9iP
def Arp1Ta2( a1, a2  ): return  _np.arctan2( a1, a2)
def Arp2Ta2( a1, a2  ): return  _np.arctan2( a2, a1)
def Arp_Ta2( a0, a1  ):
    if       a0  == 0 :
        if   a1  == 0 : arp  =    0.0      # 冇
        elif a1  >= 0 : arp  =  _ZDuPLI
        else          : arp  = -_ZDuPLI    # ldy < 0      
    else              :
        arp = _np.arctan(a1/a0)
        if   a0  >  0 : return  arp
        if  arp  >  0 : arp -=  _ZDuPAI
        else          : arp +=  _ZDuPAI           
    return  arp

Arp_ = {
  'n' : DatSelf,
  'd' : Arp_De9
}

# 二维空间旋转 rot-2d rotation (原点转)
def Da2SRot( at, ro,     fc='n'):
    return  _np.dot(da2, _ZH_RO2(Arp_[fc](rot)))
# 二维空间转移 rot-2d rotation & re-location
def Da2SRit( at, ro, lo, fc='n'):
    return  vbb(Da2SRot( at, ro, fc) +
            _np.expand_dims( lo, 0 ) )
# 二维空间弧转 
def Da2_ars( ga, ls,     ro= 0 ):
    _ga  =   ga/  2.0            # 半角
    _gv  =   1 /_ga              #
    _za  =  _ga* ls
    _gd  =  _gv*_np.sin(_za)
    _la  =  _ZDuPAI  - (_za + ro)
    return _np.stack([-_gd * _np.cos(_la), _gd * _np.sin(_la)], -1)
