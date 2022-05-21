from django.contrib import admin

from .models import GreenCard, BlueCard, table, user

class GreenCardAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields' : ('text', 'card_type')
        }),
        ('Выпуск продукции 1 мес', {
            'classes': ('collapse',),
            'fields' : ('count_prod', 'price_prod')
        }),
        ('Распродажа', {
            'classes': ('collapse',),
            'fields' : ('discount',)
        }),
        ('Выручка', {
            'classes': ('collapse',),
            'fields' : ('earnings', 'price_earn')
        }),
        ('Оптовый контракт 1 мес', {
            'classes': ('collapse',),
            'fields' : ('count_opt', 'earnings_opt')
        }),
        ('Оптовый контракт 2 мес', {
            'classes': ('collapse',),
            'fields' : ('count_opt_1', 'price_opt_1', 'count_opt_2', 'price_opt_2')
        }),
        ('Онлайн заказы', {
            'classes': ('collapse',),
            'fields' : ('count_online', 'price_online', 'percents')
        })
    )

class BlueCardAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields' : ('text', 'card_type')
        }),
        ('Бонус к зарплате', {
            'classes': ('collapse',),
            'fields': ('salary_percent',)
        }),
        ('Штрафы (налоги, регистрация)', {
            'classes': ('collapse',),
            'fields': ('fines',)
        }),
        ('Покупка онлайн-магазина', {
            'classes': ('collapse',),
            'fields': ('online_shop',)
        }),
        ('Траты на рекламу (СММ)', {
            'classes': ('collapse',),
            'fields': ('ads_percent',)
        }),
        ('Закупка оборудования', {
            'classes': ('collapse',),
            'fields': ('equip',)
        }),
        ('Уволился 1 программист', {
            'classes': ('collapse',),
            'fields': ('fired_percent',)
        }),
        ('Повышение цен на компоненты', {
            'classes': ('collapse',),
            'fields': ('detector_percent', 'price_percent')
        }),
        ('Доп. обучение сотрудников', {
            'classes': ('collapse',),
            'fields': ('education',)
        }),
        ('Выставка', {
            'classes': ('collapse',),
            'fields': ('hospitality_1', 'hospitality_2', 'hospitality_3')
        }),
    )

admin.site.register(GreenCard, GreenCardAdmin)
admin.site.register(BlueCard, BlueCardAdmin)
admin.site.register(table)
admin.site.register(user)
