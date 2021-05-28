import general.models


def show_template_debugging(draft_tag: str) -> str:
    """
    When rendering some information about a branch (address, phone, email etc.),
    show a special sign if in GeneralSettings "Template debugging" is turned on.

    This sign is just to make sure that this piece of information is really
    rendered from database rather than hardcoded in HTML.
    """

    # //@formatter:off
    # Assertions {
    assert isinstance(draft_tag, str)
    # } Assertions
    # //@formatter:on

    general_settings = general.models.GeneralSettings.objects.get(pk="general_settings")

    result = draft_tag

    if general_settings.template_debugging:
        result += "<span class='template-debugging'> [[ &#xb6; ]] </span>"

    # //@formatter:off
    # Assertions {
    assert isinstance(result, str)
    # } Assertions
    # //@formatter:on

    return result
