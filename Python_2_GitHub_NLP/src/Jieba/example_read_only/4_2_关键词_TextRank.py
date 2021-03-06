# coding=utf-8
'''
Created on 2016年4月12日
@author: 李健博
程序作用：

'''
from __future__ import division
from __future__ import unicode_literals

import sys

import jieba.analyse
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

sentence='''上周，国内热轧卷板市场价格继续阴跌前行。截至5月29日，国内主要市场3.0mm普卷周平均价格为2457元/吨，较前一周下跌10元/吨；5.5mm普卷周平均价格为2528元/吨，较前一周下跌7元/吨。  近期，实体经济资金状况仍难好转，多数热钱流入股市。5月份，热轧卷板市场的涨情成为泡影。在钢厂陆续复产后，一旦各地市场资源补充到位，极有可能诱发新一轮的竞价甩货。不过，更加让人关注的是，5月份的需求释放期爽约，终端方面采购订单大幅减少，导致市场价格一直难有支撑。  分地区来看，上海热轧卷板市场价格盘整观望。据了解，现3.0mm以下规格1500mm普卷严重缺货，价格较1250mm普卷高出近百元，1250mm普卷资源则价格低廉，且需求不佳。目前，该市场库存下降速度有所放缓。截至5月29日，上海热轧卷板库存为77.84万吨，较前一周减少1.7万吨。另外，新资源正加紧到货，代理商担忧，河北钢铁集团承钢及日照钢铁等后结算资源到货后，极有可能对后市造成冲击。现货市场总体出货一般，部分商家成交较清淡，大户出货量也仅在1000吨出头。经过整个5月份的调整，市场心态逐渐转为悲观。现Q2355.5mm普卷主流报价为2380元/吨~2400元/吨。  天津热轧卷板价格震荡滑落。由于天津市场前期库存偏低，且钢厂到货较差，周初市场价格一直保持坚挺。月底市场资金压力倍增，加之期货走势欠佳，后半周天津热轧卷板价格破位下行，轻松失守2400元/吨的整数关口，且成交依然清淡。资源方面，薄卷依然短缺，4.75mm及5.75mm等中间规格普卷极为紧俏，而5.5mm等规格的普厚卷资源相对充裕，市场不乏2400元/吨以下的出货者，不同规格资源价差较大。库存方面变化不大，整体在11.2万吨左右，较前一周增加0.2万吨。近日包钢传出检修计划，在以包钢资源为主导的天津、北京地区，未来一段时间供应将收紧，成为市场为数不多的支撑点。当前天津热轧卷板价格与周边地区相比处于偏高水平，大厂资源价格过高，很难成交，价格仍有回落空间。  乐从热轧卷板市场继续探底。截至5月29日，之前领跌于市场的钢银、欧浦等电商平台报价目前暂稳，基本与主流价格持平。商家出货量一般，部分大户出货量在700吨~800吨。据了解，现在乐从市场部分规格资源紧缺，但需求比较疲软，价格无法坚挺，尤其4.0mm以下薄卷成交较差，实际交易中普遍有让价。库存方面，临近月底，钢厂资源到货量不是很多，加上持续降雨天气，2.75mm薄卷到货量更少，只有涟钢仅存一点资源，市场报价混乱。由于价格持续下跌，商家观望情绪较为浓厚，代理商缩减了订货量。预计6月中上旬乐从市场的销售压力会适度缓解。  综合来看，实体经济仍处于下行通道，短期内缺少有力的利好刺激，终端需求疲软依旧，商家信心明显不足，热轧卷板市场价格下行压力大。不过，在铁矿石价格高位震荡、钢坯回落速度缓慢的时候，成本支撑成为了近期的一个利好。综上所述，预计短期内热轧卷板价格仍将以震荡偏弱为主。
'''
top_words=jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
for word in top_words:
    print word