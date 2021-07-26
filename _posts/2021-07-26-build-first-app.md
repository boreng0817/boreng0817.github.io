---
layout: post
title: "Build my first app" 
date: 2021-07-26 23:22:00 -0700
categories: app 
---
<h1>Build my first app</h1> 


드디어 kotlin을 사용해서 앱 만들기에 도전해보았습니다. 여기까지 꽤 오랜 시간이 걸렸네요!

![fig1](https://boreng0817.github.io/asset/TIL/2021-07-26/fig1.PNG)


[Build Your First Android App in Kotlin](https://developer.android.com/codelabs/build-your-first-android-app-kotlin#0) <br>
위 링크에 있는 튜토리얼을 따라 앱을 만들면, 사진과 같은 앱이 만들어집니다.

우선 기본적으로 튜토리얼을 쭉 따라 앱을 만들어 보았고, 기능을 더해 추가로 구현한 부분까지 잘 정리해보겠습니다.

저는 이 튜토리얼에서 이걸 배웠습니다.
* Android studio에서 app build하기
* 노트북에 기기를 연결하여 앱 실행해보기
* 반응하는 button 만들기
* Android app을 만들기 위한 XML 이해하기
* Button을 이용하여 두번째 screen (Second fragment)로 이동하기

추가로
* 내 입맛대로 기능 구현해보기
* 에러 해결하기 (DEX file error)
* 에러에게 혼나기 (binding)
* 알아낸 팁(undo history)


<h3>Android studio에서 app build하기</h3>

해당 튜토리얼에서 미리 만들어둔 template를 골라 앱을 만들었습니다.
Templated을 이용하기 위해서 아래와 같은 순서로 project를 만들었습니다.
1. Android Studio를 엽니다.
2. 새로운 창에 있는 Start a new Android Studio project를 누릅니다.
3. **Basic Activity**를 고르고 **Next**를 누릅니다.
![fig2](https://boreng0817.github.io/asset/TIL/2021-07-26/fig2.PNG)
4. 적당한 이름을 지어줍시다. 저는 **My Application**으로 정했습니다.
5. **Language**는 **Kotlin**으로 정해둡시다.
6. 나머지 어렵게 생긴 것들은 건드리지 않고 **Finish**를 누릅니다.

이런 순서로 project를 만들면, Android Studio가 열심히 일을 앱을 만들어줄 준비를 합니다.

실행을 해보면 투박하지만 앱 같은 것이 만들어집니다.

![fig3](https://boreng0817.github.io/asset/TIL/2021-07-26/fig3.PNG)

<h3>노트북에 기기를 연결하여 앱 실행해보기</h3>

Android Studio는 안드로이드 기반의 핸드폰이 없는 경우를 위해 Emulator를 준비해두었습니다. <br>
이것을 사용하여 여러 실험도 해보고 실행도 시켜볼 수 있지만, 생각보다 성능을 많이 잡아 먹는 친구입니다.

그래서 집에 안 쓰는 안드로이드 공기계나, 혹은 자신이 직접 안드로이드 핸드폰을 쓴다면 노트북에 연결하여 앱을 실행하고 실험해볼 수 있습니다.

Android 4.2 이상의 핸드폰에서 개발자 모드를 통해 **USB Debugging**을 켜두면 앱을 기기에 설치하여 실행 결과를 확인할 수 있습니다. 속도도 빠르고 노트북도 좋아합니다!

저의 경우는 Android Studio에서 이런 준비를 했습니다.
1. 상단 메뉴에 있는 **Tools > SDK Manager**을 선택합니다.
2. SDK Tools를 선택합니다.
![fig4](https://boreng0817.github.io/asset/TIL/2021-07-26/fig4.PNG)
3. **Google USB Driver**을 선택하고 **Apply** 혹은 **OK**를 눌러 설치해줍니다.
![fig5](https://boreng0817.github.io/asset/TIL/2021-07-26/fig5.PNG)
4. 무언가 설치가 끝나면 이제 USB를 들어 핸드폰과 노트북/데스크탑을 연결해줍니다.

별다른 준비 없이 기기만 준비되면 연결이 되기도하고 제가 준비한대로 준비해도 연결이 되지 않는 경우도 있습니다. <br>
그 경우 [링크](https://developer.android.com/studio/run/device)에서 제공하는 해결책을 따라해보세요! 

연결에 성공했다면 기기에서 컴퓨터를 통한 디버깅을 허용하는 RSA키를 수락할지 묻는 대화상자를 표시합니다. 이를 승인하면 이제 기기에서 앱 실행을 할 수 있습니다!

<h3>반응하는 button 만들기</h3>
<h3>Android app을 만들기 위한 XML 이해하기</h3>
<h3>Button을 이용하여 두번째 screen (Second fragment)로 이동하기</h3>


<details><summary>code</summary>
</details>
