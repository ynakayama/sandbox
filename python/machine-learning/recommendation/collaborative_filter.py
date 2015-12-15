from recommendation_data import dataset
from math import sqrt

print(("山田さんのカレーの評価 : {}".format(
    dataset['山田']['カレー'])))
print(("山田さんのうどんの評価 : {}\n".format(
    dataset['山田']['うどん'])))
print(("佐藤さんのカレーの評価: {}".format(
    dataset['佐藤']['カレー'])))
print(("佐藤さんのうどんの評価: {}\n".format(
    dataset['佐藤']['うどん'])))

print("鈴木さんのレーティング: {}\n".format((dataset['鈴木'])))

# 協調フィルタリングの実装

def similarity_score(person1, person2):

    # 戻り値は person1 と person2 のユークリッド距離

    both_viewed = {}  # 双方に共通のアイテムを取得

    for item in dataset[person1]:
        if item in dataset[person2]:
            both_viewed[item] = 1

    # 共通のアイテムを持っていなければ 0 を返す
    if len(both_viewed) == 0:
        return 0

    # ユークリッド距離の計算
    sum_of_eclidean_distance = []

    for item in dataset[person1]:
        if item in dataset[person2]:
            sum_of_eclidean_distance.append(
                pow(dataset[person1][item] - dataset[person2][item], 2))
    total_of_eclidean_distance = sum(sum_of_eclidean_distance)

    return 1 / (1 + sqrt(total_of_eclidean_distance))

print("山田さんと鈴木さんの類似度 (ユークリッド距離)",
      similarity_score('山田', '鈴木'))


def pearson_correlation(person1, person2):

    # 両方のアイテムを取得
    both_rated = {}
    for item in dataset[person1]:
        if item in dataset[person2]:
            both_rated[item] = 1

    number_of_ratings = len(both_rated)

    # 共通のアイテムがあるかチェック、無ければ 0 を返す
    if number_of_ratings == 0:
        return 0

    # 各ユーザーのすべての付リファレンスを追加
    person1_preferences_sum = sum(
        [dataset[person1][item] for item in both_rated])
    person2_preferences_sum = sum(
        [dataset[person2][item] for item in both_rated])

    # 各ユーザーの嗜好の二乗を計算
    person1_square_preferences_sum = sum(
        [pow(dataset[person1][item], 2) for item in both_rated])
    person2_square_preferences_sum = sum(
        [pow(dataset[person2][item], 2) for item in both_rated])

    # 商品の価値を算出して合計
    product_sum_of_both_users = sum(
        [dataset[person1][item] * dataset[person2][item] for item in both_rated])

    # ピアソンスコアの計算
    numerator_value = product_sum_of_both_users - \
        (person1_preferences_sum * person2_preferences_sum / number_of_ratings)
    denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum, 2) / number_of_ratings) * (
        person2_square_preferences_sum - pow(person2_preferences_sum, 2) / number_of_ratings))
    if denominator_value == 0:
        return 0
    else:
        r = numerator_value / denominator_value
        return r

print("山田さんと田中さんの類似度 (ピアソン相関係数)",
      (pearson_correlation('山田', '田中')))


def most_similar_users(person, number_of_users):
    # 似たユーザーとその類似度を返す
    scores = [(pearson_correlation(person, other_person), other_person)
              for other_person in dataset if other_person != person]

    # 最高の類似度の人物が最初になるようにソートする
    scores.sort()
    scores.reverse()
    return scores[0:number_of_users]

print("山田さんに似た人ベスト 3",
      most_similar_users('山田', 3))


def user_reommendations(person):

    # 他のユーザーの加重平均によるランキングから推薦を求める
    totals = {}
    simSums = {}
    # rankings_list = []
    for other in dataset:
        # 自分自身は比較しない
        if other == person:
            continue
        sim = pearson_correlation(person, other)
        # print ">>>>>>>",sim

        # ゼロ以下のスコアは無視する
        if sim <= 0:
            continue
        for item in dataset[other]:

            # まだ所持していないアイテムのスコア
            if item not in dataset[person] or dataset[person][item] == 0:

                # Similrity * スコア
                totals.setdefault(item, 0)
                totals[item] += dataset[other][item] * sim
                # 類似度の和
                simSums.setdefault(item, 0)
                simSums[item] += sim

        # 正規化されたリストを作成

    rankings = [(total / simSums[item], item)
                for item, total in list(totals.items())]
    rankings.sort()
    rankings.reverse()
    # 推薦アイテムを返す
    recommendataions_list = [
        recommend_item for score, recommend_item in rankings]
    return recommendataions_list

print("下林さんにおすすめのメニュー",
      user_reommendations('下林'))
