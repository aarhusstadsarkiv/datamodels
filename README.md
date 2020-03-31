[![Aarhus Stadsarkiv](https://raw.githubusercontent.com/aarhusstadsarkiv/py-template/master/img/logo.png)](https://www.aarhusstadsarkiv.dk/)
# datamodels
Datamodels based on [pydantic](https://github.com/samuelcolvin/pydantic/) used in Python tools developed at Aarhus Stadsarkiv.

#### Structure
Each model is placed in a separate `.py` file in order to achieve maintainability and better version control. In addition, each model must be served in `__init__.py` such that it is possible to call `from datamodels import model`.

#### Versioning
- **Updating** a model is considered a **patch** version, e.g. `0.1.0 -> 0.1.1`
- **Adding** a model is considered a **minor** version, e.g. `0.1.0 -> 0.2.0`

Major versions will be pushed when models have reached a yet to be determined mature stage.
