# လုပ်ဆောင်  [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20out%20this%20project&url=https://github.com/thetwinhtwe/todo.project.django.myanmar&hashtags=todo,project,myanmar,opensource)
"လုပ်ဆောင်" ဆိုတာ Django သင်ခန်းစာ To Do Application ကို မြန်မာလို အဓိပ္ပါယ်ဖွင့်ဆိုချက်များနဲ့ သင်ထောက်ကူ အခြေပြုရေးသားထားတဲ့ အသုံးချ နည်းပညာ လုပ်ဆောင်ချက် ဖြစ်ပါတယ်။

![Github License](https://img.shields.io/badge/license-MIT-green)
![Bulma Version](https://img.shields.io/badge/Bulma-v0.9.1-blue)
![Django Version](https://img.shields.io/badge/Django-v3.1-green)
![Font Awesome Version](https://img.shields.io/badge/Font%20Awesome-v5-orange)

## မာတိကာ

- [**မိတ်ဆက်**](#မိတ်ဆက်)
- [လိုအပ်သည်များသွင်းယူရန်](#လိုအပ်သည်များသွင်းယူရန်)
- [ပူးပေါင်းပါဝင်တည်ဆောက်သူများ](#ပူးပေါင်းပါဝင်တည်ဆောက်သူများ)
- [လိုင်စင်](#လိုင်စင်)
- [အကူအညီ](#အကူအညီလိုပါက)

## မိတ်ဆက်

"လုပ်ဆောင်" သည် Python 3.8 နည်းပညာနှင့် Django Framework version 3.1 နှင့် ရေးသားထားခြင်းဖြစ်ပြီး စမ်းသပ် သုံးစွဲမည်ဆိုပါက Python နှင့် Django ကို သွင်းယူရမည်ဖြစ်ပါသည်။ အသုံးပြုနိုင်မည့် အချက်များမှာ 
1. လုပ်ဆောင်ချက် များ [ထည့်သွင်း]ခြင်း
2. လုပ်ဆောင်ချက် များ [ပြင်ဆင်]ခြင်း
3. လုပ်ဆောင်ချက် များ [ဖျက်သိိမ်း]ခြင်းတို့ ဖြစ်ပါသည်။

### လိုအပ်သည်များသွင်းယူရန်
ပထမဦးဆုံး ပြုလုပ်ရန်မှာ မိမိစက်တွင် python3 ရှိမရှိ ဆန်းစစ်ရန် ဖြစ်ပါသည်။

```console
python3 -V
```
ထိုနောက်မိမိထည့်သွင်းမည့် နေရာစီစဥ်ပီးပါက 

```console
git clone https://github.com/thetwinhtwe/todo.project.django.myanmar.git
```
```console
cd todo.project.django.myanmar
```
ထိုနောက်တွင် virtual environment  ကို သွင်းယူပေးရန်လိုအပ်ပါသည်။

```console
python3 -m venv env
```
ပြီးလျှင် pip ကို သွင်းရပါမည်။ ရှိပြီးလျှင် သွင်းဖို့မလိုပါ။

```console
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
ထိုမှတစ်ဆင့်

```console
source env/bin/activate
```
ဆိုပြီး virtual environment ကို activate လုပ်ပေးပါ။ ထို့နောက်တွင်

```console
python3 -m pip install -r requirements.txt
```
ဆိုလျှင် သွင်းယူမှု ပြီးစီးပါပြီ။ virtual environment ကို အသုံးမပြုတော့လျှင် ပြန်ပိတ်ပေးရပါမည်။

```console
deactivate
```

### အသုံးပြုနည်း
virtual env ကို activate အရင်လုပ်ပါ
```console
source env/bin/activate
```
ထို့နောက်တွင်
```console
python manage.py runserver
```
ဆိုလျှင်အဆင်ပြေပါပြီ

## အသုံးပြုနည်းပညာများ

Django v3.1 , Bulma v0.9.1 , Font Awesome v5.15.1

## ပူးပေါင်းပါဝင်ခြင်း

မည်သူမဆို ပူးပေါင်းပါဝင် ရေးသားနိုင်ပါသည်။ လူတိုင်း ဝင်ရောက်ရေးသားနိုင်ရန် ဖိတ်ခေါ်ပါသည်။ 

## ပူးပေါင်းပါဝင်တည်ဆောက်သူများ

[သက်ဝင်းထွေး](http://www.thet.win)

##  [ဆွေးနွေးချက်များ ပြုလုပ်ခြင်း](https://github.com/thetwinhtwe/todo.project.django.myanmar/issues)

နည်းပညာဆိုင်ရာ ချွတ်ယွင်းမှုများ၊ ပြန်လည်ပြုပြင်ချက်များ ၊ အကြံပြုချက်များကို ပြုလုပ်နိုင်ပါသည်။ ပိုမိုကောင်းမွန်သော လူ့ဘောင်အဖွဲ့အစည်းသို့ ဦးတည်၍ လိုအပ်ချက်များကို အတူတူဖြည့်စည်းခြင်းဖြင့် ရှေ့ဆက်လိုပါသည်။ 

## လိုင်စင်

ဤ project သည် [MIT License](https://github.com/thetwinhtwe/todo.project.django.myanmar/blob/version1/LICENSE) ၏ အောက်တွင် အကျုံးဝင်ပါသည်။

## အကူအညီလိုပါက

- ဆက်သွယ်ရန်မှာ email@thet.win (သို့မဟုတ်)
- [ဤတွင်လည်း](https://github.com/thetwinhtwe/todo.project.django.myanmar/issues) နှိပ်၍ ဆွေးနွေးချက်များဖြင့် ဆွေးနွေးနိုင်ပါသည်။
