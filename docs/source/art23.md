# Art23 schema

Diagrame for art23:

```{mermaid}

classDiagram
    class Contact {
        +conName
        +conInstitution
        +conPhone
        +conEmail
    }

    class MSSummary {
        +situationAt
        +nipObligation
        +a3comp .. a8comp
        +riskAssessment
        +proContribution
    }

    class Derogation {
        +a3_2DeadlineExt
        +a6_3DeadlineExt
        +a6_4DeadlineExt
        +a7_4DeadlineExt
    }

    class UWWTP {
        +uwwCode
        +uwwName
        +uwwStatus
        +uwwMeasure
        +uwwInv
        +uwwPROFund
    }

    class Agglomeration {
        +aggCode
        +aggName
        +aggStatus
        +aggMeasure
        +aggInv
    }

    class OtherInvestment {
        +invStartYear
        +invEndYear
        +invCS1b, invCS1c
        +invWWTP1b, invWWTP1c
        +invEUFund
    }

    class MonitoringResults {
        +uwwCode
        +determinand
        +performance
        +method
    }

    MSSummary "1" ..> "0..1" Derogation : conditional (not fully compliant)
    MSSummary "1" ..> "0..*" UWWTP : conditional (not fully compliant)
    MSSummary "1" ..> "0..*" Agglomeration : conditional (not fully compliant)
    MSSummary "1" ..> "0..1" OtherInvestment : conditional (not fully compliant)
    UWWTP "1" --> "0..*" MonitoringResults : uwwCode (FK)
    OtherInvestment ..> UWWTP : reconciles with total investment
    OtherInvestment ..> Agglomeration : reconciles with total investment
    UWWTP ..> Agglomeration : plant serves agglomeration (no FK in this schema)
    Derogation ..> UWWTP : a7_4 counts should reconcile
    Derogation ..> Agglomeration : a3_2 / a6_3 counts should reconcile
    MSSummary ..> UWWTP : proContribution feeds uwwPROFund
```