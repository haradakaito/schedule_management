# マルチカレンダー統合通知システム
## はじめに
私の所属する研究室のカレンダーには，当然自分以外の予定が大量に混在している．  
そのため，自分の参加する予定のみを抽出して，毎日通知してくれるシステムを作りたいと思った．  
また，研究室のカレンダー以外にも，自分だけの予定を管理しているカレンダーもある．  
別々のカレンダーを統合して，自身に関係のある予定のみを抽出して，毎日決まった時刻に通知してくれるシステムを作成した．  

## 全体概要図
![全体概要図](https://github.com/user-attachments/assets/1a92a28b-c9a8-4152-ae48-ba01b77b8f77)

## 使用技術
- AWS（Amazon Web Services）
- Python
- GoogleCalendar
- LINE Notify
- Koyeb

※ AWSでは，Event Bridge，Lambdaの二つのサービスを利用

## アルゴリズム
1. 6:00にAWS Event BridgeからLambdaにトリガーを発生させる
2. Lambdaは，KoyebにデプロイしてあるAPIを実行する
3. APIは，icalリンクから各カレンダーの直近2日分の予定を取得して返す
4. Lambdaは，API実行後，LINE Notifyを用いて取得した予定を整形し，通知する
5. 1~4を毎日繰り返す
