from typing import Union

from django.core.cache import cache

import general.const


class CacheManager:
    @staticmethod
    def cache_smth(cached_object: Union[general.const.FileExtensions],
                   a_path: Union[str, None] = None,
                   some_data: Union[str, None] = None,
                   ) -> None:
        """
        If a path is provided, data will be read from a file.
        """

        # //@formatter:off
        # Assertions {
        assert isinstance(a_path, (str, type(None)))
        assert isinstance(
            cached_object in [general.const.FileExtensions.CSS,
                              general.const.FileExtensions.JS, ])
        assert isinstance(some_data, (str, type(None)))
        assert a_path or some_data, "Either a path or data must be supplied"
        # } Assertions
        # //@formatter:on

        if not some_data:
            with open(a_path) as f:
                some_data = f.read()

        assert bool(some_data)

        cached_object_value = cache.get(cached_object.value)

        combined_data = "{}{}{}".format(cached_object_value, " ", some_data)
        cache.set(cached_object.value, combined_data)
