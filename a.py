import streamlit as sl
import datetime

sl.title("Actors ranking")

def get_response_from_chatgpt():
    pass

def main():
    user_name = sl.text_input("Họ và Tên")
    user_sex = sl.text_input("Giới tính")
    user_sex = sl.date_input("Ngày sinh",
                             min_value=datetime.date(1950, 1, 1),
                             max_value=datetime.date(2030, 1, 1))
    user_number = sl.number_input("Con số yêu thích",
                                  value=0,
                                  format='%d')
    your_number = 1
    if sl.button("Xem bói em với"):
        if user_number == 1:
            respons_text = '''
                            § ĐIỀM MẠNH CỦA BẠN:

                            - Bạn là người có trực giác rất mạnh. Trên thực tế, bạn có trực giác nhạy bén nhất trong tất cả các số. Bạn rất nhạy cảm và có một khả năng thấu hiểu người khác tuyệt vời, và có thể
                            cảm nhận rất nhiều về những gì đang xảy ra đằng sau hậu trường. Ví dụ, bạn sẽ nhận biết về mối quan hệ và sức khỏe của mọi người dù không được nói cho biết bất cứ điều gì. Bạn ở
                            đây để sử dụng món quà trực giác và sự nhạy cảm để giúp đỡ người khác.

                            - Con số đường đời số 11 có những phẩm chất của số 2 được khuếch đại.

                            - Bạn là con người của tình yêu, sự khoan dung, đồng cảm, lắng nghe, hòa bình, kết nối.

                            - Bạn sẵn lòng tha thứ cho người khác nếu họ biết lỗi. Bạn không những thấu hiểu mà còn đồng cảm được với niềm vui hoặc nỗi buồn của người khác khi họ tâm sự với bạn, làm cho
                            họ được vơi đi.

                            - Bạn có thể dành hàng giờ chỉ để ngồi nghe họ tâm sự. Bạn còn có thể kết nối bạn bè của bạn với những người khác để giúp mọi người. Bạn là chuyên gia kết nối.

                            - Bạn là người sinh ra để yêu và được yêu; coi trọng tình cảm, gia đình, tình bạn. Bạn khát khao tình yêu. Bạn muốn được mọi người đối xử bằng tình yêu thương, sự dịu dàng trong lời
                            nói và hành động.

                            - Bạn cũng luôn trao đi tình yêu thương, tình cảm tới mọi người và luôn mong cho mọi người được bình an, hòa thuận và hạnh phúc.

                            - Bạn thực sự là người bạn chân thành, tâm lý và vô cùng an toàn. Đối với bạn, tình yêu, gia đình và bạn bè là những điều không thể thiếu trong cuộc sống.

                            - Là người hòa giải, bạn có nhiều giải pháp và luôn hành động để hóa giải xung đột, đối đầu. Bạn thường là người có những hành động, việc làm để hòa giải những người đang có vấn
                            đề xung đột với nhau. Bạn không bao giờ đành lòng nhìn thấy bạn bè mình có sự mâu thuẫn, cãi vã. Bạn không thích, thậm chí là sợ bất kỳ hình thức đổ vỡ nào.

                            - Bạn có năng lực tâm linh, trực giác tốt. Cảm nhận của bạn về một điều gì đó thường là chính xác. Bạn có thể có những giấc mơ biến thành sự thật, có tham vọng lớn; bạn có thể cảm
                            nhận được năng lượng, v.v..

                            - Nếu bạn có con số này bạn là người có nhận thức về tâm linh, có tầm nhìn xa, đầy cảm hứng, lôi cuốn, sáng tạo, một người mơ mộng, lý tưởng, và suy nghĩ sâu sắc. Và bạn dựa vào
                            đức tin chứ không phải logic để đối phó với cuộc sống và tất cả những gì nó đem lại.

                            § ĐIỀM YẾU CỦA BẠN:

                            - Thách thức đối với bạn là không để bản thân bị áp đảo bời chính những món quà của bạn. Nỗi sợ hãi và ám ảnh sẽ là nhược điểm của con số này. Đôi khi bạn cũng có thể trông như
                            thiếu quyết đoán, không thực tế, thần kinh và thất thường.

                            - Quá yêu thương sẽ làm cho bạn dễ bị kiệt sức, bởi bạn thường xuyên phải giải quyết, tư vấn, níu kéo để tránh sự đổ vỡ nào đó. Bạn sợ bị từ chối, bởi với bạn, đó là biểu hiện của sự
                            rạn nứt.

                            - Quá cảm xúc nên bạn có thể sẽ không kiểm soát được tâm trạng, nhất là khi bị khủng hoảng.

                            - Bạn làm việc và đối xử tốt với người khác. Bạn có khả năng kết hôn sớm, cam kết và trung thành cho cả cuộc đời. Tuy vậy, thật không may là bạn thường bị quyến rũ bởi những hấp
                            lực mang nặng tính đời trần (hỉ nộ ái ố, yêu yêu hận hận...) để rồi xa lìa mục đích cao cả của mình.

                            - Bạn cũng dễ suy sụp và mất phương hướng nếu không tự hiểu được chính mình. Bạn có nhiều tham vọng hướng tới những điều lớn lao và khả năng để đạt được chúng, nhưng nếu
                            không thể tự tin thì những mong muốn đó sẽ thất bại.

                            - Có những sự khác biệt cực kỳ to lớn giữa cách sống của những người Số 11 nào biết sống tích cực và vận dụng được sức mạnh tâm linh vượt trội của mình vào giúp ích cuộc sống, và
                            những người Số 11 đầy tiêu cực với đời sống có vẻ đầy khó khăn và nhạt nhòa.
                            - NHỮNG NGƯỜI NỒI TIẾNG CÓ SỐ 11/2:
                            
                            - Wolfgang Amadeus Mozart, Harry Houdini, Michelle Obama, David Beckham

                            Bên cạnh số đường đời, sẽ còn hơn 20 chỉ số quan trọng khác phân tích chỉ tiết về bạn, đặc biệt bạn xem kĩ các chỉ số ðở biểu đồ kim tự tháp để xem các năm đỉnh cao trong cuộc đời
                            và biểu đồ sức mạnh để xem các giá trị năng lực mà bạn có cùng với các chỉ số khác kèm lời khuyên tương ứng để kích hoạt được các điểm mạnh của bạn giúp bạn phát triển, gặp
                            nhiều thuận lợi trong cuộc sống.

                            Mối quan hệ tương thích

                            § MỐI QUAN HỆ NÓI CHUNG TRONG CUỘC SỐNG:

                            Số đường đời tương thích nhất với bạn:

                            - Số 2: Số 11 và 2 với nhau là sự kết hợp hoàn hảo vì cả hai có mối liên hệ chặt chẽ với nhau. Cả hai này có cùng một ngôn ngữ, giao tiếp ngoại giao và mong muốn một mối quan hệ
                            hài hòa.

                            - Số 6: Người bảo vệ số 6 có thể cung cấp cho bạn một mối quan hệ tốt và bạn sẵn sàng chấp nhận để họ cời mỡ về tình cảm.

                            - Số 8: Sự kết hợp này là một ví dụ về thu hút sự đối lập. Trực giác cao của bạn sẽ bổ sung cho số 8 một cách mạnh mẽ để ra quyết định.

                            Số đường đời ít tương thích với bạn:

                            - Số 10: Trực giác cùng sự quan tâm của bạn sẽ gây những tác động tiêu cực đến số 10.

                            - Số 3: Số 3 đôi khi kém kỷ luật có thể khiến bạn thường xuyên phải nhắc nhờ sự chềnh mảng của họ. Tuy nhiên, sự lạc quan của số 3 có thể mang lại chút nhẹ nhõm cho bạn.

                            - Số 4 (hoặc 22/4): Số 4 mang tính ổn định nên ban đầu có vẻ phù hợp với bạn, nhưng việc thiếu biểu hiện cảm xúc của số 4 sẽ không kết nối với bạn theo đúng cách.

                            - Số 5: Những người số 5 mạo hiểm chắc chắn sẽ không ngại có những mối quan hệ với những người số 11 như bạn, nhưng bản tính thiếu trách nhiệm của họ có thể vô tình làm tổn
                            thương nếu bạn là người nhạy cảm cao.

                            - Số 7: Trí tuệ tri thức của số 7 thường không hoạt động tốt với trí tuệ cảm xúc của bạn (khía cạnh số 2 của bạn), nhưng sự rung động tinh thần mạnh mẽ của bạn (khía cạnh số 11 của
                            bạn) có thể thu hút số 7 để cùng tìm kiếm sự thật.

                            - Số 9: Ghép nối bạn với số 9 có thể hiệu quả vì cả hai đều tìm kiếm sự thỏa mãn từ lòng vị tha, nhưng bản chất xa cách của số 9 có thể quá lạnh lùng đối với bạn.

                            Hãy nhớ rằng khả năng tương thích trong các mối quan hệ của bạn còn sâu sắc hơn những gì thể hiện ở con số đường đời. Để biết cách tạo ra sự hài hòa, bạn sẽ cần xem xét các con
                            số khác trong thần số học của mình. Chỉ số Linh hồn, Sứ mệnh, Nhân cách và Thái độ của bạn cũng sẽ ảnh hưởng đến mức độ tương thích của bạn trong các mối quan hệ. Đọc thêm
                            các luận giải về các chỉ số này để tạo ra một bức tranh tổng quát cho bạn.

                            § TÌNH DUYEN:

                            - Số 11 là một phiên bản tăng cường của số 2, có nghĩa là bạn đồng cảm và nhạy cảm với những người trong cuộc sống của bạn giống như những người có đường đời số 2. Bạn là
                            những người giao tiếp, lắng nghe tốt và luôn phấn đấu đề có được sự hòa hợp trong mọi môi trường. Điều bất lợi là năng lực tâm linh làm bạn có thể bận tâm đến các cõi khác và quên
                            đi mối quan hệ với những người ở đây trên trái đất.

                            - Bạn là một người hòa bình và sẵn sàng thỏa hiệp trong một mối quan hệ, và bạn coi trọng sự đồng hành. Điều này khiến bạn trở thành một người bạn đồng hành tuyệt vời với bạn
                            đời.
                            - Vì đường đời sô 11 nhạy cảm tâm linh và trực giác cao nhất trong tất cả các sồ đường đời, nên việc đáp ứng nhu cầu của bạn đời là điều đương nhiên. Bạn cũng vô cùng chung thủy.
                            Sự cam kết và lòng trung thành rất quan trọng đối với bạn, và các mối quan hệ của bạn thể hiện nhiều yếu tố tỉnh thần.

                            - Bạn là người giàu cảm xúc và đôi khi dễ bị lo lắng và trầm cảm. Bạn có thể được hưởng lợi từ một người bạn đời tính tình ổn định có thể khơi dậy ngọn lửa tình cảm bằng một chút
                            đồng cảm.

                            - Bạn là người yêu thương và tốt bụng, nhưng cũng cần không gian riêng và có tính cách độc lập mạnh mẽ, vì vậy những người bạn đời "nhạt" quá sẽ khiến bạn kiệt sức. Nhưng khi
                            bạn đời làm tổn thương bạn (cố ý hoặc vô tình), bạn có thể phản ứng bằng một sức mạnh cảm xúc sâu sắc.

                            Cách tiếp cận tình cảm của bạn cũng sẽ bị ảnh hưởng bởi các con số khác trong biểu đồ. Chỉ số Linh hồn, chỉ số Nhân Cách, chỉ số Thái độ và Chỉ số Sứ mệnh sẽ thay đổi cách cuộc
                            sống tình cảm của bạn diễn ra. Hãy đọc tiếp tới các chỉ số này.
                            '''
            return sl.write(f"{respons_text}")
    
main()