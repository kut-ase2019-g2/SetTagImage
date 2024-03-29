# -*- coding: utf-8 -*-
from psychopy import visual, core, event, gui, data, misc
import numpy, os, random, time, csv, glob, re

img = glob.glob('img/*')
numpy.random.shuffle(img)

changeEn = {
    u'キラキラ':'KiraKira',
    u'ハート':'Heart',
    u'音符':'Notes',
    u'炎':'Fire',
    u'集中線':'Central_line',
    u'波紋':'Rain',
    u'電撃':'Thunder',
    u'レンズフレア':'Lens_flare',
    u'漫画風':'Comicalize',
    u'振動':'Blur',
    u'コントラスト':'Change_contrast',
    u'拡大':'Zoom_in',
    u'縮小':'Zoom_out'
    
    
    }

try:
    # 参加者IDの取得
    try:
        expInfo = misc.fromFile('lastParams.pickle')
    except:
        expInfo = {'Participant':'001'}

    expInfo['dateStr']= data.getDateStr()
    dlg = gui.DlgFromDict(expInfo, title='Experiment', fixed=['dateStr'])
    if dlg.OK:
        misc.toFile('lastParams.pickle', expInfo)
    else:
        core.quit()

    # Windowの準備
    myWin = visual.Window(fullscr=True, monitor='Default', allowGUI=False, units='norm', color=(1,1,1))

    # 結果を保存する場所を準備
    results=[]

    # 教示をだす。
    instructionStr = u"""\
今から、表示される画像に適切だと思うタグを選択してください。

左のタグが適切なら、キーボードのFを押してください。
右のタグが適切なら、キーボードのJを押してください。

この教示が読めたら、「スペース」キーを押して課題を始めてください"""
    instText = visual.TextStim(myWin, text=instructionStr,pos=(0,0), color=(-1,-1,-1), height=0.08)
    instText.font = 'ヒラギノ角ゴシック W5'
    instText.draw()
    myWin.flip()
    # 参加者がspaceキーを押すまで画面を出したまま待つ。
    keyList = event.waitKeys(keyList=['space'])

    # 参加者の反応をリセット
    Responded = None

    for i in range(len(img)):
        tag = [u'キラキラ', u'ハート', u'音符', u'炎', u'集中線', u'波紋', u'電撃', u'レンズフレア', u'漫画風', u'振動', u'コントラスト', u'拡大', u'縮小']
        k = len(tag)-1
        myImg = visual.ImageStim(myWin, image=img[i], pos=(0,0.3), units='norm',size = [1,1])
        imgN = visual.TextStim(myWin, text=str(i+1)+'/'+str(len(img)),pos=(0.9,-0.9), color=(-1,-1,-1), height=0.05)
        while k > 0:
            #print(tag)
            numpy.random.shuffle(tag)
            # テキストの準備
            leftText = visual.TextStim(myWin, text=str(tag[0]), pos=(-0.5,-0.7), color=(-1,-1,-1), colorSpace='rgb', height=0.2)
            leftText.font = 'ヒラギノ角ゴシック W5'
            rightText = visual.TextStim(myWin, text=str(tag[1]), pos=(0.5,-0.7), color=(-1,-1,-1), colorSpace='rgb', height=0.2)
            rightText.font = 'ヒラギノ角ゴシック W5'
            tagN = visual.TextStim(myWin, text=str(len(tag)-1),pos=(0.9,0.9), color=(-1,-1,-1), height=0.05)
            # テキストの書き込み
            myImg.draw()
            leftText.draw()
            rightText.draw()
            imgN.draw()
            tagN.draw()
            # 提示
            myWin.flip()

            # 参加者の反応測定開始
            # 前回の刺激提示の影響を消去する
            event.clearEvents()
            # 参加者の反応をリセット
            Responded = None
            Responded = event.waitKeys(keyList=['f','j','r','q'])
            if Responded[0] == 'f':
                tag.pop(1)
            elif Responded[0] == 'j':
                tag.pop(0)
            elif Responded[0] == 'r':
                tag = [u'キラキラ', u'ハート', u'音符', u'炎', u'集中線', u'波紋', u'電撃', u'レンズフレア', u'漫画風', u'振動', u'コントラスト', u'拡大', u'縮小']
                k = len(tag)-1
            elif Responded[0] == 'q':
                core.quit()
            # 参加者の反応測定終了
            k = len(tag)-1

            # 中視点の準備
            myText = visual.TextStim(myWin,text = '+',pos=(0,0),color = (-1,-1,-1),height=0.2)
            myText.draw()
            #　画面表示
            myWin.flip()
            core.wait(0.1)

        # 英語に変換する
        tag[0] = re.sub('({})'.format('|'.join(map(re.escape, changeEn.keys()))), lambda m: changeEn[m.group()], tag[0])
        # 1画像に対する結果の保存
        results.append([
            img[i],
            tag[0]
            ])

    # 最終的な結果を保存
    curD = os.getcwd()
    datafile = open(os.path.join(curD, 'Tag_data', 'Sub{0}_{1}.csv'.format(expInfo['Participant'], expInfo[ 'dateStr'])),'wb')
    datafile.write('File name, Tag name\n'.encode('shift-jis'))
    for r in results:
        datafile.write('{0}, {1}\n'.format(*r).encode('shift-jis'))
    datafile.close()

except TypeError as e:
    print (e)
