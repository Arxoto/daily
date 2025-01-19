# SSE Edit

https://www.nexusmods.com/skyrimspecialedition/mods/164

## Magic Effect

see https://ck.uesp.net/wiki/Magic_Effect

```
Record Header
EDID - Editor ID                唯一标识 根据 ESP 排序前几位可能改变 后几位在内部固定
VMAD - Virtual Machine Adapter
FULL - Name                     显示名称
MDOB - Menu Display Object      菜单显示效果
KSIZ - Keyword Count            关键字数量
KWDA - Keywords                 关键字，不做任何事，用于条件函数和调用游戏系统赋予的效果
Magic Effect Data               效果
    DATA - Data
        Flags (sorted)  标签，用于特殊逻辑
            Hostile  被敌对，恢复术不要点
            Detrimental  取负值，恢复术点了会扣血
            Recover  效果结束时返回初始状态，数值修改器和峰值修改器会在开始时修改、结束时改回，即对恢复术来说，选中是buff，不选是治疗
            FX Persist  视觉效果持续到结束，不选只有一次
            Snap to Navmesh  选中此项将会在使用 Aimed 或 Target_Location 时把效果附在 Navmesh 上（此处你可以理解为地面上），一般用于召唤物
            No Recast  选中时此效果时在效果结束前不能在目标上再次释放
            No Hit Effect  不会出现命中时的视觉效果
            No Death Dispel  如果目标已死亡效果也仍然触发
            No Duration  没有持续时间，瞬时触发
            No Hit Event  不会触发命中事件，主要用于潜行系技能
            No Magnitude  效果不使用 Magnitude 字段（？）
            No Area  取消区域判定
            Painless  无痛，如果同时选中 Hostile 则目标不会喊疼，如果目标是玩家不会出现视觉模糊和呻吟
            Gory Visuals  没有使用，没效果
            Hide in UI  魔法效果将不会出现在法术描述和魔法效果那一栏里
            Power Affects Magnitude  在wiki中没有解释
        Base Cost  法术消耗的乘数，不影响自动计算的法术消耗（https://ck.uesp.net/wiki/Spell#Notes）
        Assoc. Item  与Effect_Archetype有关
        Magic Skill  受哪一系法术perk影响，并为其提供经验
        Resist Value  受抗性影响
        Counter Effect count
        Casting Light  蓄力时手中光效
        Taper Weight  持续时间结束后，效果保留一段时间但强度减弱，称为锥度持续时间，这是锥度权重
        Hit Shader  命中时shader（理解为光效）
        Enchant Shader  附魔时的光效
        Minimum Skill Level  NPC使用效果的最低要求，同时影响法术等级，0新手、25学徒、50熟练、75专家、100大师
        Spellmaking  Magnitude/Duration perk影响范围还是持续时间
            Area  效果影响面积？
            Casting Time  施法时间？
        Taper Curve  锥度曲线，控制效果减弱的速度
            - 当前大小 = 效果大小 * 锥度权重 * (1-时间/锥度持续时间)^锥度曲线
            - magnitude = effect magnitude * Taper Weight * (1 - taper time / Taper Duration)Taper Curve
            - 总大小（仅当锥度曲线>-1） = 效果大小 * 锥度权重 * 锥度持续时间 / (锥度曲线+1)
            - magnitude = effect magnitude * Taper Weight * Taper Duration / (Taper Curve + 1)
            - 锥度曲线=0 效果保持不变
            - 锥度曲线=1 效果线性递减
            - 锥度曲线越大 下降越快 负数意味着增加 但不建议小于-1
        Taper Duration  锥度持续时间
        Second AV Weight
        Archtype  在wiki中没解释 应该是修改类型 参考 "Peak Value Modifier"
        Actor Value  在wiki中没解释 应该是角色属性修改 参考 
            - 强化生命[MGEF:000493AA]  强化体力[MGEF:00049507]  强化法力[MGEF:00049504]
            - "Health"                 "Stamina"                "Magicka"                 属性值上限
            - "Heal Rate"              "Stamina Rate"           "Magicka Rate"            属性恢复速度（设为10，每秒恢复10%）
            - "Heal Rate Mult"         "Stamina Rate Mult"      "Magicka Rate Mult"       属性恢复速度提升（设为100，每秒恢复翻倍）
            - 强化负重[MGEF:0007A0F4]
            - "Carry Weight" 负重上限
            - 强化龙吼[MGEF:0008850D]  龙吼计时[MGEF:0401DF9A]
            - "Shout Recovery Mult" 龙吼恢复速率 建议为 20% 倍数（大多冷却时间为5的倍数）
        Projectile  飞行物，子弹，若添加了多个则只生效第一个
        Explosion  子弹命中时产生的爆炸物
        Casting Type  如何触发
            - Concentration 按住持续施放
            - Fire_and_Forget 蓄力后施放
            - Constant_Effects 恒定效果
            - 法术或结界的所有效果必须具有相同的施法类型
        Delivery  效果如何传递到目标
            - Self 施法者自身
            - Contact 接触，通过命中触发，只能用于武器，一般用于附魔
            - Aimed 瞄准，将效果附加在Projectile（子弹）上，命中时触发效果，如大火球爆炸
            - Target_Actor 目标角色，立刻作用于准星上的角色，第三人称时不好用
            - Target_Location 目标物体景观，同上，无Projectile，如寒霜符文
            - 法术或结界的所有效果必须具有相同的传递类型
        Second Actor Value
        Casting Art  蓄力时手中特效
        Hit Effect Art  命中时特效
        Impact Data  子弹击中物体时使用哪些贴花
        Skill Usage Multiplier  收获经验的乘数
        Dual Casting
            Art  双手施法时的特效
            Scale  双手施法时的范围
        Enchant Art  附魔时的特效
        Unknown
        Unknown
        Equip Ability  效果被装备时的行为（？），不可链式触发
        Image Space Modifier  效果触发时的图像空间（也是特效）
        Perk to Apply  仅为玩家使用，触发效果时添加perk
        Casting Sound Level  在wiki中没有解释，猜测是蓄力时的声音，影响潜行被发现
        Script Effect Al  敌人AI
            Score  越大使用越频繁
            Delay Time  冷却
Counter Effects                不使用
SNDD - Sounds
DNAM - Magic Item Description  描述 <mag> 效果大小（增幅） <dur> 持续时间 <area> 范围
Conditions
```

