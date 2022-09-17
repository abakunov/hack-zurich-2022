# import requests
# import os
# import re
# from core.models import *



# cookies = {
#     'fvgs_ml': 'mosaic',
#     'Zalando-Client-Id': 'cbee5c89-2e8d-489c-91b6-1fd7923abfeb',
#     'mpulseinject': 'false',
#     'bm_sz': 'A30C77CF7D53B1C75F7294DF3DB39A35~YAAQJJpkXzi+M0yDAQAAMu4VTRE51iRExeuCofexqq58CAt2hi9ffHCPjgfLRqgskrktdyemxc50py8MUCYEuiv8HZ+Q+xqh1Je9ws17VsRhAF67x6SzKmsm6F+2PC0Kuku4oaUpvTTYagfyukymFX1WjUckBr1162wQKrUMQ36n0ir0IXtCKITxNwgWz8FHMFwtInzxT+jwcKzlo3dntTJMINCSQMWy9C8dPxTEUizrrkv1GRKZ4Dw8iLh4rvWeR2AcVWxAe3MyVD9dM2z4A/VCjDnyH0Wnrymvix3H2WoURutcN7g3USuD4QqwcMJJJkraLkLlO3EufFVQV2gpVUX8KUV5cgjJOE5iqCEt87CnmifOHnonTMUmUiFFm3I7bgK5~3162680~4602165',
#     'bm_mi': 'A622F0249EC831B6892915DC6FDE322C~YAAQJJpkX1e+M0yDAQAAxPAVTRFV3rieLDchIEzgNpewQUGjNfo/ryIYhGxyGEN0WhDK3RBBsM8N1Cn7HrFLUbqlZzU0rfa+cARqvNMdIzqla70aBuFc0Kj3zzGVaPEaTS6Adf3MUB1BpFF8IG8nGI0PfrQHfxUN5NKs6qqtHaowdyqzxyybWo4sv3ob4VnGXao9c0zgkG95/ALBaVK75WmbEldJ5AzHwvi4Gd/SbNDWG787fDokVx8RxtadZSTVMJ1Yg1Hen28z51tq60cD4gno11gQ1uiq4cpi59W7rRbxib6b6kClqQyRYZK9~1',
#     'language-preference': 'da',
#     'ak_bmsc': '2A8ABEC7A7BD189803B8C2BD0848133B~000000000000000000000000000000~YAAQJJpkX7G+M0yDAQAAGPYVTRFN5xngRaCxQuzi5bOGmq8dzalkIPioZ5vk0jbsHZ5ggcmkP2DNrfgDeT6UkKMf/ebu1TO/WqxZdzBrzeqq968uXSzuHpXiGtzTZSwbARSpqBfPnkwl3oucgSWFAPv61/9KPQp1k56L/9+ncGLDCECQIiMtb6T4ey7L5JYP/WVzWQ7Rn5Ktl0iOdR3GtQQiY9QB7qY1ELQg1p7zqYYhIiTNWd+g7uLnUvLR3uArB0oLEQFTTSVOUd23/J6Hegosh9Tt4wPL8sclXjb31UD2C6imFThWA34LcTD5LCw5/AVC3UECmLN4JL5Txyga8djvdzQrk0vdKkQzY78fqttjJXxrMg/XQpV4Iw1ySt//v4Mck9oj5iDraJgWqkLo6HYfC+TDEngubuXlNGwkC94Fs97K43bw+ny2qTqJWtOA9t03uJXtW+YmzvGnTpnjVMIIQUt1ZFjd80ldhkfE8i0n4in3qnTDDl5Tq6XKk1OP',
#     '_gcl_au': '1.1.649208744.1663445637',
#     'sqt_cap': '1663445627388',
#     '_ga': 'GA1.2.506774501.1663445637',
#     '_gid': 'GA1.2.248003707.1663445637',
#     '_fbp': 'fb.1.1663446322136.2078032114',
#     'ncx': 'm',
#     'catalog.follow_brand_banner_re': '%7B%22count%22%3A3%2C%22isClosed%22%3Atrue%7D',
#     'frsx': 'AAAAAGJ2y0g9WbMLnjN-_QQInwSe1Q7OOq4c8G05zH6uMreaIQDiGFpAs9BiWK0oj_7ZKB5Tpyj9oTHZ7xVZsslsVx4JpfESvZQQL9S6V8VYSTc8frUs5t3tlUd35v7EZR9J9WQXrh5HnatD7X4S8I0=',
#     '_gat_zalga': '1',
#     '_abck': '736B5C37A91E8DBB4FE8983A443C51FD~-1~YAAQax1BF0xct0uDAQAAq/tGTQgovXbauFwLgGNqx3SrILGaA38SIdac3syXf8kq43l+Yk19OHTOUhsSqp5CkMni0vrR0+RjcaUg7MzyTYpG6rdSj8kgP6fA2+zryg69E4UHklkSofpM4ppcOeGrfqKh7/D7RP2dU96ksDlcsWw0j/qEXaA2jdcKdkyQo8+wZ6jDRCkLeuUnf61zEuvDmrRtn92/sKgg4OTtsZie11g0QUPXQiISp37deXyP2aqwjuspB8gWv7hne5ZhDzStmEAWRul+rsPeeKzUd92ggGWCTF2b90KuW+rLmiNJiyaXJQQDmsCYjGbTC/NIzY/Pxi2b1SsMo80mDrmiB6tJ2VPS154nuwyonDoFRPb0jOy8iqNqPHON9fw27gh9uNPTAC4oQLV8APpB/Ce4aQ5JH8Z/+fG32OI3j3cMbwg5T2Q7WZuIBymwoO/cw227mouN1LaZO6h6JKZo1hMJ6cW7iu6xhw==~-1~-1~-1',
#     'bm_sv': 'D156BCF772E2B78463F0A095606C4BBF~YAAQax1BF29ct0uDAQAAgf1GTRHAUKa3yJbZ4tq7Mx2Ql5WTue+nidLbp+ifMWs5NAbElrTdPKXZuKe4bYNmZHD0LkmlaEowt2/em/8wJ+knDXgX/vlfb7KonaP3qVp8jjjeDKRCnQhl2AjDrmSW+CebTY1WjZmlFTOgyPECrrB+s1f5fr2oatFpIn18TsbC5LFrmYd2QBKFhwPxYMaJa0FWSPeJVzVdB+ByG6nNjVYV7S2I+ZxKiJZrFPaV3QxGlsAR+pA3z+TG~1',
# }

# headers = {
#     'authority': 'www.zalando.dk',
#     'accept': '*/*',
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     # Already added when you pass json=
#     # 'content-type': 'application/json',
#     # Requests sorts cookies= alphabetically
#     # 'cookie': 'fvgs_ml=mosaic; Zalando-Client-Id=cbee5c89-2e8d-489c-91b6-1fd7923abfeb; mpulseinject=false; bm_sz=A30C77CF7D53B1C75F7294DF3DB39A35~YAAQJJpkXzi+M0yDAQAAMu4VTRE51iRExeuCofexqq58CAt2hi9ffHCPjgfLRqgskrktdyemxc50py8MUCYEuiv8HZ+Q+xqh1Je9ws17VsRhAF67x6SzKmsm6F+2PC0Kuku4oaUpvTTYagfyukymFX1WjUckBr1162wQKrUMQ36n0ir0IXtCKITxNwgWz8FHMFwtInzxT+jwcKzlo3dntTJMINCSQMWy9C8dPxTEUizrrkv1GRKZ4Dw8iLh4rvWeR2AcVWxAe3MyVD9dM2z4A/VCjDnyH0Wnrymvix3H2WoURutcN7g3USuD4QqwcMJJJkraLkLlO3EufFVQV2gpVUX8KUV5cgjJOE5iqCEt87CnmifOHnonTMUmUiFFm3I7bgK5~3162680~4602165; bm_mi=A622F0249EC831B6892915DC6FDE322C~YAAQJJpkX1e+M0yDAQAAxPAVTRFV3rieLDchIEzgNpewQUGjNfo/ryIYhGxyGEN0WhDK3RBBsM8N1Cn7HrFLUbqlZzU0rfa+cARqvNMdIzqla70aBuFc0Kj3zzGVaPEaTS6Adf3MUB1BpFF8IG8nGI0PfrQHfxUN5NKs6qqtHaowdyqzxyybWo4sv3ob4VnGXao9c0zgkG95/ALBaVK75WmbEldJ5AzHwvi4Gd/SbNDWG787fDokVx8RxtadZSTVMJ1Yg1Hen28z51tq60cD4gno11gQ1uiq4cpi59W7rRbxib6b6kClqQyRYZK9~1; language-preference=da; ak_bmsc=2A8ABEC7A7BD189803B8C2BD0848133B~000000000000000000000000000000~YAAQJJpkX7G+M0yDAQAAGPYVTRFN5xngRaCxQuzi5bOGmq8dzalkIPioZ5vk0jbsHZ5ggcmkP2DNrfgDeT6UkKMf/ebu1TO/WqxZdzBrzeqq968uXSzuHpXiGtzTZSwbARSpqBfPnkwl3oucgSWFAPv61/9KPQp1k56L/9+ncGLDCECQIiMtb6T4ey7L5JYP/WVzWQ7Rn5Ktl0iOdR3GtQQiY9QB7qY1ELQg1p7zqYYhIiTNWd+g7uLnUvLR3uArB0oLEQFTTSVOUd23/J6Hegosh9Tt4wPL8sclXjb31UD2C6imFThWA34LcTD5LCw5/AVC3UECmLN4JL5Txyga8djvdzQrk0vdKkQzY78fqttjJXxrMg/XQpV4Iw1ySt//v4Mck9oj5iDraJgWqkLo6HYfC+TDEngubuXlNGwkC94Fs97K43bw+ny2qTqJWtOA9t03uJXtW+YmzvGnTpnjVMIIQUt1ZFjd80ldhkfE8i0n4in3qnTDDl5Tq6XKk1OP; _gcl_au=1.1.649208744.1663445637; sqt_cap=1663445627388; _ga=GA1.2.506774501.1663445637; _gid=GA1.2.248003707.1663445637; _fbp=fb.1.1663446322136.2078032114; ncx=m; catalog.follow_brand_banner_re=%7B%22count%22%3A3%2C%22isClosed%22%3Atrue%7D; frsx=AAAAAGJ2y0g9WbMLnjN-_QQInwSe1Q7OOq4c8G05zH6uMreaIQDiGFpAs9BiWK0oj_7ZKB5Tpyj9oTHZ7xVZsslsVx4JpfESvZQQL9S6V8VYSTc8frUs5t3tlUd35v7EZR9J9WQXrh5HnatD7X4S8I0=; _gat_zalga=1; _abck=736B5C37A91E8DBB4FE8983A443C51FD~-1~YAAQax1BF0xct0uDAQAAq/tGTQgovXbauFwLgGNqx3SrILGaA38SIdac3syXf8kq43l+Yk19OHTOUhsSqp5CkMni0vrR0+RjcaUg7MzyTYpG6rdSj8kgP6fA2+zryg69E4UHklkSofpM4ppcOeGrfqKh7/D7RP2dU96ksDlcsWw0j/qEXaA2jdcKdkyQo8+wZ6jDRCkLeuUnf61zEuvDmrRtn92/sKgg4OTtsZie11g0QUPXQiISp37deXyP2aqwjuspB8gWv7hne5ZhDzStmEAWRul+rsPeeKzUd92ggGWCTF2b90KuW+rLmiNJiyaXJQQDmsCYjGbTC/NIzY/Pxi2b1SsMo80mDrmiB6tJ2VPS154nuwyonDoFRPb0jOy8iqNqPHON9fw27gh9uNPTAC4oQLV8APpB/Ce4aQ5JH8Z/+fG32OI3j3cMbwg5T2Q7WZuIBymwoO/cw227mouN1LaZO6h6JKZo1hMJ6cW7iu6xhw==~-1~-1~-1; bm_sv=D156BCF772E2B78463F0A095606C4BBF~YAAQax1BF29ct0uDAQAAgf1GTRHAUKa3yJbZ4tq7Mx2Ql5WTue+nidLbp+ifMWs5NAbElrTdPKXZuKe4bYNmZHD0LkmlaEowt2/em/8wJ+knDXgX/vlfb7KonaP3qVp8jjjeDKRCnQhl2AjDrmSW+CebTY1WjZmlFTOgyPECrrB+s1f5fr2oatFpIn18TsbC5LFrmYd2QBKFhwPxYMaJa0FWSPeJVzVdB+ByG6nNjVYV7S2I+ZxKiJZrFPaV3QxGlsAR+pA3z+TG~1',
#     'dpr': '2',
#     'origin': 'https://www.zalando.dk',
#     'referer': 'https://www.zalando.dk/herretoej-t-shirts-og-poloer/2nd-day.8848-altitude.andiata.anerkjendt.angulus.arket.arkk-copenhagen.b-young.becksoendergaard.bertoni.billi-bi.birgitte-herskind.bisgaard.bjoern-borg.blendshe.blendshe-1.boob-design.bruun-and-stengade.bruuns-bazaar.by-garment-makers.by-malene-birger.by-malina.by-second-female.bytimo.carin-wester.casall.casual-friday.chelsea.clean-cut-copenhagen.color-kids.copenhagen-muse.copenhagen-shoes.craft.cras.cream.custommade.dagmar.daily-sports.danefa-kobenhavn.daniel-wellington.day-birger.day-et.decadent-copenhagen.dedicated.design-letters.designers-remix.didrikson.dranella.drdenim-online-shop.envii.esme-studios.estelle-and-thild.eton.filippa-k.fiveunits.foreo.fransa.freequent.gabba.garment-project.gestuz.gina-tricot-1.golden-beards.gosh-copenhagen.h2o.haglofs.halo.han-kjobenhavn.happy-socks-online-shop.helly-hansen.henrik-vibskov.hofmann-copenhagen.holzweiler.hope.hosbjerg.houdini.hummel-1.hunkydory.hust-claire.icepeak.ichi.ichi-petite.ilse-jacobsen.indicode-jeans.indiska.inwear.isbjoern-of-sweden.ivy-copenhagen.jlindeberg.joha.julie-sandlau.jumperfabriken.just-junkies.kaffe-online-shop.karen-by-simonsen.karitraa.kronstadt.larsson-and-jennings.lego-wear.les-deux.levete-room.lexington.libertine-libertine.lilboo.limited-by-name-it.lindbergh.lindex.little-liffner.loewengrip.love-copenhagen.luhta.lumene.m-by-m.mads-norgaard.mainio.makia.mamalicious.maria-black.marimekko.marmar-copenhagen.martin-asbjorn.matinique.mikk-line.mini-rodini.minimum.modstroem.molo.monki.mos-mosh.moss-copenhagen.moves.mr-bear-family.muesli-by-green-cotton.munthe.na-kd-online-shop.name-it.nellycom.nialaya.nn07.noa-noa.noisy-may-online-shop.norrona.notes-du-nord.nudie.nuemph.nunoo.object-online-shop.odd-molly.only-online-shop.only-sons.papu.part-two.pavement.peak-performance.pieces-online-shop.rains.reima.resterods.resume.rohnisch.royal-republiq.rukka.saint-tropez.samsoe-and-samsoe.sand-copenhagen.sandqvist.selahatin.selected.simply-copenhagen.skagen-online-shop.skandinavisk.smafolk.sneaky-steve.snoe-of-sweden.soaked-in-luxury.sofie-schnoor.soft-gallery.solid.soyaconcept.stella-nova.stylein.summery-copenhagen.tigerofsweden.vagabond.vero-moda.vibe-harslof.viking.vila-1.weekday.wheat.why7.won-hundred.wood-wood.yas-online-shop.zizzi-online-shop/?p=2',
#     'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#     'viewport-width': '740',
#     'x-xsrf-token': 'AAAAAGJ2y0g9WbMLnjN-_QQInwSe1Q7OOq4c8G05zH6uMreaIQDiGFpAs9BiWK0oj_7ZKB5Tpyj9oTHZ7xVZsslsVx4JpfESvZQQL9S6V8VYSTc8frUs5t3tlUd35v7EZR9J9WQXrh5HnatD7X4S8I0=',
#     'x-zalando-experiments': 'b891eec6-b3d5-4760-b685-fe1fbe3ce330=THE_LABEL_IS_ENABLED;07fb3627-d56d-4909-954d-d58607a2abd6=RES_CATALOG_ENTITIES;90aa955b-d7f6-4fe1-a14f-2522788af1bb=fdbe-release1-enabled;b951ad11-ec05-4c78-9772-1eb1100c5c96=ABB_DISABLED;cb304bd0-53f9-4d2c-9817-3fdd9e388aaa=sephora_garden_disabled;163908b6-4ba9-4442-981f-b340d4b4e9fe=experience_theme_disabled',
#     'x-zalando-feature': 'catalog',
#     'x-zalando-intent-context': 'navigationTargetGroup=MEN',
#     'x-zalando-request-uri': '/herretoej-t-shirts-og-poloer/drdenim-online-shop.gina-tricot-1.happy-socks-online-shop.hummel-1.jlindeberg.kaffe-online-shop.mamalicious.na-kd-online-shop.noisy-may-online-shop.object-online-shop.only-online-shop.pieces-online-shop.selected.skagen-online-shop.tigerofsweden.vero-moda.vila-1.yas-online-shop.zizzi-online-shop.2nd-day.8848-altitude.andiata.anerkjendt.angulus.arket.arkk-copenhagen.b-young.becksoendergaard.bertoni.billi-bi.birgitte-herskind.bisgaard.bjoern-borg.blendshe.blendshe-1.boob-design.bruun-and-stengade.bruuns-bazaar.by-garment-makers.by-malene-birger.by-malina.by-second-female.bytimo.carin-wester.casall.casual-friday.chelsea.clean-cut-copenhagen.color-kids.copenhagen-muse.copenhagen-shoes.craft.cras.cream.custommade.dagmar.daily-sports.danefa-kobenhavn.daniel-wellington.day-birger.day-et.decadent-copenhagen.dedicated.design-letters.designers-remix.didrikson.dranella.envii.esme-studios.estelle-and-thild.eton.filippa-k.fiveunits.foreo.fransa.freequent.gabba.garment-project.gestuz.golden-beards.gosh-copenhagen.h2o.haglofs.halo.han-kjobenhavn.helly-hansen.henrik-vibskov.hofmann-copenhagen.holzweiler.hope.hosbjerg.houdini.hunkydory.hust-claire.icepeak.ichi.ichi-petite.ilse-jacobsen.indicode-jeans.indiska.inwear.isbjoern-of-sweden.ivy-copenhagen.joha.julie-sandlau.jumperfabriken.just-junkies.karen-by-simonsen.karitraa.kronstadt.larsson-and-jennings.lego-wear.les-deux.levete-room.lexington.libertine-libertine.lilboo.limited-by-name-it.lindbergh.lindex.little-liffner.loewengrip.love-copenhagen.luhta.lumene.m-by-m.mads-norgaard.mainio.makia.maria-black.marimekko.marmar-copenhagen.martin-asbjorn.matinique.mikk-line.mini-rodini.minimum.modstroem.molo.monki.mos-mosh.moss-copenhagen.moves.mr-bear-family.muesli-by-green-cotton.munthe.name-it.nellycom.nialaya.nn07.noa-noa.norrona.notes-du-nord.nudie.nuemph.nunoo.odd-molly.only-sons.papu.part-two.pavement.peak-performance.rains.reima.resterods.resume.rohnisch.royal-republiq.rukka.saint-tropez.samsoe-and-samsoe.sand-copenhagen.sandqvist.selahatin.simply-copenhagen.skandinavisk.smafolk.sneaky-steve.snoe-of-sweden.soaked-in-luxury.sofie-schnoor.soft-gallery.solid.soyaconcept.stella-nova.stylein.summery-copenhagen.vagabond.vibe-harslof.viking.weekday.wheat.why7.won-hundred.wood-wood/',
# }

# json_data = [
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322S0LB-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::HU342D076-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O16S-M11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O122-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::HU342D08A-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::HU342D0AB-N11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::ARU22O001-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::BJ242D06U-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::LEP22O005-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::LEP22O005-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::WEB22O055-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O132-A13',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::WEB22O055-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SO422O0AS-C11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O0YX-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::M1422O01X-N11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O02I-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::HU342D08A-N11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::ARU22O001-A12',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::ARU22O001-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::WEB22O056-B11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::LEP22O000-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::HU342D09E-C11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SE622P050-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::M1422O01X-M12',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SE622O0R0-A13',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::HK022O021-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::M1422O01X-G11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::M1422O01X-C12',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::A2322O02A-N11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O0KW-K11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SA322O03A-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::ARU22O000-M11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::WEB210025-Q15',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::WEB22O05A-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322P02U-B11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SO422O059-K11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::WEB22O056-O11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O02I-M15',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SE622O0R0-A12',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SE622O0MA-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::LEP22O005-K11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O178-O11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::HU322O00P-C11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::LIQ22O015-B11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O132-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::HU322O01N-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::WEB22O05O-Q15',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O16Z-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O132-A12',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::LEP22O001-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O174-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::ARU22O000-C17',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SE622P03H-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::WEB22O05A-O15',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SE622O0R0-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O15E-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::LEP22O005-K22',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::HU322O00P-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O15E-O13',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SE622O0QP-A12',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O16Z-K11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SE622P00O-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::WEB22O05T-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::LEP22O00B-T11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::BL522O05E-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::M1422O01Y-N11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::BL522O0AO-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::G5022O010-M11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::ARU22O001-K11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::HU342D070-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::M1422O027-K11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::PE442D02V-K11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322O0QK-Q12',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SE682Q000-K11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SE622P052-C12',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::LEP22O000-A11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::WEB22O056-O15',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SE622O0R1-Q11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::HU322O00P-K11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SO422P00K-C12',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::SO422O059-N11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::M1422O01X-P11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'e03ec0f25449bb8a5690ecd21ea0169a88afbbbbaa179ed8168b684ee7a34616',
#         'variables': {
#             'id': 'ern:product::OS322P02Z-K11',
#             'skipHoverData': False,
#         },
#     },
#     {
#         'id': 'f94e5655c018fed674b09926218ce63e176b493128e7b1f2087e3a98e35b18ad',
#         'variables': {
#             'id': 'ern:outfit::4rlREEzHQV6',
#             'width': 295,
#             'reuseDataForTracking': True,
#         },
#     },
#     {
#         'id': 'f94e5655c018fed674b09926218ce63e176b493128e7b1f2087e3a98e35b18ad',
#         'variables': {
#             'id': 'ern:outfit::JhBu5kcDR_-',
#             'width': 295,
#             'reuseDataForTracking': True,
#         },
#     },
#     {
#         'id': 'f94e5655c018fed674b09926218ce63e176b493128e7b1f2087e3a98e35b18ad',
#         'variables': {
#             'id': 'ern:outfit::M5Bs731jTQ2',
#             'width': 295,
#             'reuseDataForTracking': True,
#         },
#     },
#     {
#         'id': 'e3af64bfb551a5cde72b767c29fcfff031de8e96529d0d2e1515259c3c4d6201',
#         'variables': {
#             'id': 'ern:campaign:cfa:851ced77-c19b-4f3d-9b1a-b7580ffc1229:4bbd40e1-d1e8-4418-8903-80d679c280b6',
#             'reuseDataForTracking': True,
#             'hideCarousel': True,
#         },
#     },
#     {
#         'id': 'd09a9412472a12a2ce1e3ae6d2ece307c341d35a8584fd64acd22021fcdca881',
#         'variables': {
#             'id': 'ern:campaign:cfa:3b7be5a0-e34e-4ef1-b282-240dd795c865:4bbd40e1-d1e8-4418-8903-80d679c280b6',
#         },
#     },
#     {
#         'id': '3451b6709c0ba525d4f1895ee0692317e7c383c2749ee81ba2dfe3e88d44919d',
#         'variables': {
#             'id': 'ern:campaign:cfa:3b7be5a0-e34e-4ef1-b282-240dd795c865:4bbd40e1-d1e8-4418-8903-80d679c280b6',
#         },
#     },
#     {
#         'id': 'e3af64bfb551a5cde72b767c29fcfff031de8e96529d0d2e1515259c3c4d6201',
#         'variables': {
#             'id': 'ern:campaign:cfa:71fe382d-4c7d-4fea-a460-ca600b53657e:4bbd40e1-d1e8-4418-8903-80d679c280b6',
#             'reuseDataForTracking': True,
#             'hideCarousel': True,
#         },
#     },
# ]

# response = requests.post('https://www.zalando.dk/api/graphql/', cookies=cookies, headers=headers, json=json_data).json()

# def start():
#     for good in response:
#         try:
#             name = good['data']['product']['name']
#             brand = good['data']['product']['brand']['name']
#             image_url = re.findall("(.*\.jpg).*", good['data']['product']['largeDefaultMedia']['uri'])[0]
#             link = good['data']['product']['uri']
#             price = int(good['data']['product']['displayPrice']['original']['formatted'][:-6])
#             silhouette = good['data']['product']['silhouette']
#             print(price)
#         except Exception as e:
#             pass
