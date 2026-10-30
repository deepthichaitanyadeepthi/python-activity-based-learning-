
``` mermaid
flowchart TD
    A([START]) --> B[/Enter Patient Name and Age/]
    B --> C[/Enter Consultation Charge/]
    C --> D[/Enter Diagnostic Charge/]
    D --> E[/Enter Treatment Charge/]
    E --> F{Are Charges Negative?}

    F -- Yes --> G[/Display Invalid Charges/]
    G --> Z([STOP])

    F -- No --> H[Calculate Total Bill]
    H --> I{Total >= 10000?}

    I -- Yes --> J[Apply 10% Discount]
    I -- No --> K{Total >= 5000?}

    K -- Yes --> L[Apply 5% Discount]
    K -- No --> M[No Discount]

    J --> N[Calculate Final Bill]
    L --> N
    M --> N

    N --> O[/Display Final Bill/]
    O --> P[/Enter Amount Paid/]
    P --> Q{Payment < 0 or Payment > Final Bill?}

    Q -- Yes --> R[/Display Invalid Payment/]
    R --> Z

    Q -- No --> S[Calculate Balance]
    S --> T{Balance == 0?}

    T -- Yes --> U[/Fully Paid/]
    T -- No --> V{Amount Paid > 0?}

    V -- Yes --> W[/Partially Paid/]
    V -- No --> X[/Unpaid/]

    U --> Y[/Display Payment Details/]
    W --> Y
    X --> Y

    Y --> Z([STOP])

```
