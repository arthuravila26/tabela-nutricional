from pydantic import BaseModel


class Calculate(BaseModel):
    quantity: float

    # description = description.split('&')
    # data = {}
    # for i in description:
    #     d = TabelaService().get_description(i)
    #     data[i] = d