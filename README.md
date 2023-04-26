[Maciel Calebe Vidal, Dr](https://www.linkedin.com/in/macielvidal/). Megadados.
[Insper](https://www.insper.edu.br), 2023.

# Mini IMDB

Hello World!

## Usage

To use this application, please follow these steps:

1.  Set up your environment and install the required libraries by running the following commands:
    - On Linux/macOS:
        ```sh
        python3 -m venv .venv
        pip install -r requirements.txt
        source ./venv/Scripts/activate
        ```
    - On Windows
        ```ps
        python -m venv .venv
        pip install -r requirements.txt
        .\venv\Scripts\activate
        ```

2.  Create an environment variables file by running one of the following commands, depending on your operating system:
    - On Linux/macOS/PowerShell
        ```sh
        mv .env.example .env
        ```
    - On Windows CMD
        ```cmd
        move .env.example .env
        ```
3.  Fill the `.env` file with the actual acees credentials to your database.

4. To start the server with auto-reload, run the following command:
    ```sh
    uvicorn src:app --reload
    ```

## Authors

<table width="100%">
    <tr>
        <td align="center">
            <a href="https://github.com/felipeschiavinato"><img src="https://github.com/felipeschiavinato.png" style="width: 50%;" /></a>
        </td>
        <td align="center">
            <a href="https://github.com/FelixLuciano"><img src="https://github.com/FelixLuciano.png" style="width: 50%;" /><br /></a>
        </td>
    </tr>
    <tr>
        <td align="center">
            <a href="https://github.com/felipeschiavinato"><strong>Felipe Schiavinato</strong></a>
        </td>
        <td align="center">
            <a href="https://github.com/FelixLuciano"><strong>Luciano Felix</strong></a>
        </td>
    </tr>
</table>

## License

This code is MIT Licensed! [See the LICENSE file](LICENSE) for details.
