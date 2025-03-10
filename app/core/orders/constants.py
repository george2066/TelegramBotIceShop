from enum import StrEnum

class OrderStatusEnum(StrEnum):
    unlisted = "unlisted" # пользователь заполняет заказ
    ordered = "ordered" # заказ передали официанту
    done = "done" # заказ отдали гостю